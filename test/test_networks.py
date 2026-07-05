'''
test_networks.py (unittest)

common/networks.py의 RobotInterface, PLCInterface를 벤더 SDK
(IndyDCPClient, pymcprotocol.Type3E) 모킹으로 검증한다.
실물 로봇·PLC·네트워크 연결 없이 실행 가능하다.

실행 방법:
    python -m unittest test_networks.py -v
'''

import unittest
from unittest.mock import MagicMock, patch

from config import robot01_config


class TestRobotInterface(unittest.TestCase):

    def setUp(self):
        # common.networks가 참조하는 IndyDCPClient 자리를 매 테스트마다 새로 모킹
        patcher = patch('common.networks.IndyDCPClient')
        self.addCleanup(patcher.stop)
        self.MockIndyClass = patcher.start()

        self.mock_indy = MagicMock()
        self.mock_indy.connect.return_value = True   # 기본값: 연결 성공
        self.MockIndyClass.return_value = self.mock_indy

        from common.networks import RobotInterface
        self.robot = RobotInterface(robot01_config.ROBOT_IP, robot01_config.ROBOT_NAME)

    def test_connect_success_sets_connected_flag(self):
        self.robot.connect()
        self.mock_indy.connect.assert_called_once()
        self.assertTrue(self.robot._is_connected)

    def test_connect_failure_does_not_set_connected_flag(self):
        self.mock_indy.connect.return_value = False   # 연결 실패 재현
        self.robot.connect()
        self.assertFalse(
            self.robot._is_connected,
            "connect() 실패 시 _is_connected가 True로 잘못 설정되면 안 됨 (은폐된 실패 방지)"
        )

    def test_connect_twice_does_not_reconnect(self):
        self.robot.connect()
        self.robot.connect()   # 이미 연결된 상태에서 재호출
        self.mock_indy.connect.assert_called_once()   # 실제 connect는 1회만 호출되어야 함

    def test_disconnect_calls_indy_disconnect(self):
        self.robot.connect()
        self.robot.disconnect()
        self.mock_indy.disconnect.assert_called_once()
        self.assertFalse(self.robot._is_connected)

    def test_disconnect_without_connect_does_nothing(self):
        self.robot.disconnect()   # 연결한 적 없는 상태에서 호출
        self.mock_indy.disconnect.assert_not_called()


class TestPLCInterface(unittest.TestCase):

    def setUp(self):
        patcher = patch('common.networks.Type3E')
        self.addCleanup(patcher.stop)
        self.MockType3EClass = patcher.start()

        self.mock_plc = MagicMock()
        self.MockType3EClass.return_value = self.mock_plc

        from common.networks import PLCInterface
        from config import plc_config
        self.plc = PLCInterface(plc_config.PLC_IP, plc_config.PLC_PORT)

    def test_connect_calls_plc_connect_with_ip_port(self):
        self.plc.connect()
        self.mock_plc.connect.assert_called_once_with(self.plc.plc_ip, self.plc.plc_port)
        self.assertTrue(self.plc._is_connected)

    def test_close_calls_plc_close(self):
        self.plc.connect()
        self.plc.close()
        self.mock_plc.close.assert_called_once()
        self.assertFalse(self.plc._is_connected)

    def test_read_bit_returns_raw_plc_value(self):
        self.mock_plc.batchread_bitunits.return_value = [1]
        result = self.plc.read_bit("Y23")
        self.mock_plc.batchread_bitunits.assert_called_once_with("Y23", 1)
        self.assertEqual(result, 1)

    def test_write_bit_true_sends_1(self):
        self.plc.write_bit("X14", True)
        self.mock_plc.batchwrite_bitunits.assert_called_once_with("X14", [1])

    def test_write_bit_false_sends_0(self):
        self.plc.write_bit("X14", False)
        self.mock_plc.batchwrite_bitunits.assert_called_once_with("X14", [0])


if __name__ == '__main__':
    unittest.main()
