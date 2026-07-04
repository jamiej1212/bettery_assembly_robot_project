#==============================================
#   robot_client + plc interface
#   MC프로토콜: 이더넷, Type3E
#   https://pymcprotocol.netlify.app/
#==============================================

from vendor.indy_utils import indydcp_client as client
from pymcprotocol import Type3E


# vendor.indy_utils.indydcp_client 래퍼
class RobotClient:

    def __init__(self, robot_ip: str, robot_name: str):
        self.robot_ip = robot_ip
        self.robot_name = robot_name
        self.indy = client.IndyDCPClient(self.robot_ip, self.robot_name)
        self._is_connected = False

    # ── 컨트롤러 연결/해제 ──
    def connect(self) -> None:
        if not self._is_connected:
            self.indy.connect()
            self._is_connected = True
            print('Indy7 컨트롤러와 통신이 연결되었습니다.')
        else:
            print('Indy7 컨트롤러와 이미 통신 중입니다.')

    def disconnect(self) -> None:
        if self._is_connected:
            self.indy.disconnect()
            self._is_connected = False
            print('Indy7 컨트롤러와 통신이 해제되었습니다.')
        else:
            print('Indy7 컨트롤러와 통신이 연결되어있지 않습니다.')


# pymcprotocol.Type3E 래퍼
class PLCInterface:
    def __init__(self, plc_ip: str, plc_port):
        self.plc= Type3E()
        self.plc_ip = plc_ip
        self.plc_port = plc_port
        self._is_connected = False

    def connect(self): #PLC 통신 연결
        if not self._is_connected:
            self.plc.connect(self.plc_ip, self.plc_port)
            self._is_connected = True
            print('PLC 통신이 연결되었습니다.')
        else:
            print('PLC와 이미 통신 중입니다.')

    def close(self): #PLC 통신 해제
        if self._is_connected:
            self.plc.close()
            self._is_connected = False
            print('PLC 통신이 해제되었습니다.')
        else:
            print('PLC와 통신이 연결되어있지 않습니다.')


    def read_bit(self, address): #지정 비트 디바이스 상태 조회
        start_signal = self.plc.batchread_bitunits(address, 1)[0]
        print('지정 비트 디바이스 상태 조회 완료')
        return start_signal

    def write_bit(self, address, value): #지정 비트 디바이스에 값 기록
        int_value = 1 if value else 0
        self.plc.batchwrite_bitunits(address, [int_value])
        print('비트 디바이스 단위 쓰기 완료')