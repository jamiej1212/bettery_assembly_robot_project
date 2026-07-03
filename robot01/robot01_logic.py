'''
    로봇01 공개 인터페이스(AI팀 임포트 대상)
'''

def _approach_position(base_position, retract_z):
    print('상공 진입 완료')

# ── 신호 수신 (이원화 — 최종 확정 시 한쪽만 유지) ──
def receive_start_signal_from_plc(robot, plc, config, poll_interval: float = 0.05):
    print('PLC 비트(Y23)를 직접 폴링하여 동작 시작 신호 수신 완료')

def receive_start_signal_from_ai(ai_signal_callback):
    print('AI팀이 중계한 동작 시작 신호를 콜백으로 수신 완료')


# ── 베이스 픽업 ──
def move_to_base_storage_position(robot, config):
    print('베이스 스토리지 상공 진입 완료')

def lower_to_base_storage(robot, config):
    print('베이스 스토리지 하강 완료')

def grab_base(robot, config):
    print('베이스 그리퍼 닫기 완료')

def raise_from_base_storage(robot, config):
    print('베이스 스토리지 상승 완료')


# ── 거치대 배치 ──
def move_to_conveyor_position(robot, config):
    print('거치대 상공 진입 완료')

def lower_to_conveyor(robot, config):
    print('거치대 위로 하강 완료')

def release_base(robot, config):
    print('거치대 위로 그리퍼 해제 완료')

def raise_from_conveyor(robot, config):
    print('거치대 위로 상승 완료')

# ── 판정 분기 1: 이물질/직경 불량 (재픽업 루프는 AI팀이 픽업 함수 재호출로 구현) ──
def move_to_defect_discard_position(robot, config):
    print('이물질/직경 불량 판정 후 폐기 위치 상공 진입 완료')

def lower_to_defect_discard(robot, config):
    print('이물질/직경 불량 판정 후 폐기 위치 하강 완료')

def raise_from_defect_discard(robot, config):
    print('이물질/직경 불량 판정 후 폐기 위치 상승 완료')


# ── 판정 분기 2: 각도 불량 (재검사 없이 즉시 거치대 재배치로 직행) ──
def rotate_90(robot, config):
    print('각도 불량 판정 후 각도 재설정 완료')


# ── 시퀀스 종료 ──
def return_home(robot, config):
    print('시퀀스 종료 후 홈 포지션 이동 완료')
