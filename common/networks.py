#==============================================
#   robot_client + plc interface
#   MC프로토콜: 이더넷, Type3E
#   https://pymcprotocol.netlify.app/
#==============================================

from pymcprotocol import Type3E


# vendor.indy_utils.indydcp_client 래퍼
class RobotClient:
    # ── 컨트롤러 연결/해제 ──
    def connect():
        print('Indy7 컨트롤러와 통신 연결')
    def disconnect():
        print('Indy7 컨트롤러와 통신 해제')

    # ── 모션 완료 여부 판별 ──    
    def check_move_done(poll_interval=0.1):
        print('모션 완료 여부 확인')

    # ── 로봇 동작 ──
    def move_to(position): #절대 좌표 모션 명령
        print('Indy7 모션 명령 수행')
    def move_by(offset): #상대 좌표 모션 명령
        print('Indy7 모션 명령 수행')
    def lower_by(z_offset): #하강 모션 명령
        print('Indy7 하강 모션 명령 수행')
    def raise_by(z_offset): #상승 모션 명령
        print('Indy7 상승 모션 명령 수행')
    def rotate_by(angle): #회전 모션 명령
        print('Indy7 회전 모션 명령 수행')
    def go_home(): #홈 포지션 이동 명령
        print('Indy7 홈 포지션 이동 명령 수행')

    # ── 그리퍼 동작 ──
    def grab(): #그리퍼 닫기 명령
        print('Indy7 그리퍼 닫기 명령 수행')
    def release(): #리퍼 열기 명령
        print('Indy7 그리퍼 열기 명령 수행')

    # ── 안전 제어 ──
    def pause(): #모션 일시정지 명령
        print('Indy7 모션 일시정지 명령 수행')
    def resume(): #모션 재개 명령
        print('Indy7 모션 재개 명령 수행')
    def reset_to_initial(): #초기 상태로 리셋 명령(비상정지)
        print('Indy7 초기 상태로 리셋 명령 수행')


# pymcprotocol.Type3E 래퍼
class PLCInterface:
    def connect(): #PLC 통신 연결
        print('PLC 통신 연결')

    def close(): #PLC 통신 해제
        print('PLC 통신 해제')

    def read_bit(address): #지정 비트 디바이스 상태 조회
        print('지정 비트 디바이스 상태 조회 완료')

    def write_bit(address, value): #지정 비트 디바이스에 값 기록
        print('비트 디바이스 단위 쓰기 완료')