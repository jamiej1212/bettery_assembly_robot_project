#==============================================
#   robot_client + plc interface
#   MC프로토콜: 이더넷, Type3E
#   https://pymcprotocol.netlify.app/
#==============================================

from vendor.indy_utils.indydcp_client import IndyDCPClient
from pymcprotocol import Type3E

# ── 로봇 연결 / 해제 ──
class RobotInterface:
    def __init__(self, robot_ip: str, robot_name: str):
        self.robot_ip = robot_ip
        self.robot_name = robot_name
        self.indy = IndyDCPClient(self.robot_ip, self.robot_name)
        self._is_connected = False

    # 로봇 연결
    def connect(self) -> None:
        if not self._is_connected:
            success = self.indy.connect()
            if not success:
                print('[ERROR] Indy7 컨트롤러 연결 실패 — IP/포트, 서버 실행 상태를 확인하십시오')
                return
            self._is_connected = True
            print('[INFO] Indy7 컨트롤러 통신 연결')
        else:
            print('[INFO] Indy7 컨트롤러 이미 통신 중')
            
    # 로봇 연결 해제
    def disconnect(self) -> None:
        if self._is_connected:
            self.indy.disconnect()
            self._is_connected = False
            print('[INFO] Indy7 컨트롤러 통신 해제')
        else:
            print('[INFO] Indy7 컨트롤러 통신 연결되어있지 않음')


# ── PLC 연결 / 해제 ──
class PLCInterface:
    def __init__(self, plc_ip: str, plc_port: int):
        self.plc_ip = plc_ip
        self.plc_port = plc_port
        self.plc = Type3E()
        self._is_connected = False

    def connect(self): #PLC 통신 연결
        if not self._is_connected:
            self.plc.connect(self.plc_ip, self.plc_port)
            self._is_connected = True
            print('[INFO] PLC 통신 연결')
        else:
            print('[INFO] PLC 이미 통신 중')

    def close(self): #PLC 통신 해제
        if self._is_connected:
            self.plc.close()
            self._is_connected = False
            print('[INFO] PLC 통신 해제')
        else:
            print('[INFO] PLC 통신 연결되어있지 않음')

    def read_bit(self, address: str): #지정 비트 디바이스 상태 조회
        start_signal = self.plc.batchread_bitunits(address, 1)[0]
        print(f'[INFO] {address} 디바이스 상태 조회 완료: {bool(start_signal)}')
        return start_signal

    def write_bit(self, address: str, value: bool): #지정 비트 디바이스에 값 기록
        int_value = 1 if value else 0
        self.plc.batchwrite_bitunits(address, [int_value])
        print(f'[INFO] {address} 디바이스 단위 쓰기 완료: {value}')