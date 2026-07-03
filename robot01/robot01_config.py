'''
    좌표·속도·PLC1 접속 정보(포트 1025)등 설정
'''

# ── 통신 접속 정보 ──
ROBOT1_IP = "192.168.3.6" # 로봇1(Indy7) 컨트롤러의 IP 주소
ROBOT1_NAME = "NRMK-Indy7" # Indy DCP 프로토콜상 로봇 모델을 식별하는 이름
PLC1_CONNECTION = {"plc_ip": "192.168.3.130", "plc_port": 1025} #로봇1이 사용하는 PLC 접속 정보를 담은 딕셔너리
START_SIGNAL_ADDRESS="Y23" # 스토퍼센서가 매핑된 PLC 비트 주소

# ── 위치 좌표 [x, y, z, rx, ry, rz] (TODO: 현장 티칭 후 확정) ──
CONVEYOR_PLACE_POSITION = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
BASE_STORAGE_POSITION = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
DEFECT_DISCARD_POSITION = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

# ── 모션 파라미터 ──
ROTATION_ANGLE=90 #deg 각도 불량 정렬 시 6축 회전각

# 위치별 2단 접근 오프셋(TODO: 현장 검증) - 하강 거리
CONVEYOR_RETRACT_Z = 0.05 # m 컨베이어 접근 시 상공 오프셋
BASE_STORAGE_RETRACT_Z = 0.05 # m 베이스 스토리지 접근 시 상공 오프셋
DEFECT_DISCARD_RETRACT_Z = 0.05 # m 폐기 라인 접근 시 상공 오프셋

# ── 속도 파라미터 (TODO: 실기 테스트로 단계적 확정) ──
APPROACH_SPEED = 5 # 상공 이동(자유 공간)
PRECISION_SPEED = 2 # 하강/접근/삽입(대상물 근접)
ROTATION_SPEED = 2 # 회전 이동

# ── 그리퍼 ──
GRIPPER_DO_INDEX = 0 # set_do()에 사용되는 디지털 출력 채널 번호