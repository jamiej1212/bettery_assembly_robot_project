'''
    로봇02 공개 인터페이스(AI팀 임포트 대상)
'''

def _approach_position(base_position, retract_z):
    print('상공 진입 완료')

def _slot_position(grid_params_by_type, array_type, slot_index):
    print('슬롯 좌표 계산 완료')


# ── 신호 수신 (이원화 — 최종 확정 시 한쪽만 유지) ──
def receive_start_signal_from_plc(robot, plc, config, poll_interval: float = 0.05):
    print('PLC 비트(Y24)를 직접 폴링하여 동작 시작 신호 수신 완료')

def receive_start_signal_from_ai(ai_signal_callback):
    print('AI팀이 중계한 동작 시작 신호를 콜백으로 수신 완료')


# ── 셀 픽업 및 극성 검사 (슬롯 수만큼 반복 — 반복 제어는 AI팀 소관) ──
def move_to_cell_pick_position(robot, config, array_type, slot_index):
    print('셀 픽업 위치 상공 진입 완료')

def lower_to_cell_pick(robot, config):
    print('셀 픽업 위치 하강 완료')

def grab_cell(robot, config):
    print('셀 그리퍼 닫기 완료')

def raise_from_cell_pick(robot, config):
    print('셀 픽업 위치 상승 완료')


# ── 판정 분기: 극성 불량 (폐기) ──
def move_to_polarity_discard_position(robot, config):
    print('극성 불량 판정 후 폐기 위치 상공 진입 완료')

def lower_to_polarity_discard(robot, config):
    print('극성 불량 판정 후 폐기 위치 하강 완료')

def release_cell(robot, config):
    '''셀 그리퍼 해제. 폐기·삽입 양쪽 경로에서 공통 사용'''
    print('셀 그리퍼 해제 완료')

def raise_from_polarity_discard(robot, config):
    print('극성 불량 판정 후 폐기 위치 상승 완료')


# ── 판정 분기: 극성 정상 (삽입) ──
def move_to_insertion_position(robot, config, array_type, slot_index):
    print('극성 정상 판정 후 삽입 위치 상공 진입 완료')

def lower_to_insertion(robot, config):
    print('극성 정상 판정 후 삽입 위치 하강 완료')

def raise_from_insertion(robot, config):
    print('극성 정상 판정 후 삽입 위치 상승 완료')


# ── 전체 조망 및 누락 검사 (보충은 위 픽업/삽입 함수를 재호출하여 처리) ──
def move_to_overview_position(robot, config):
    print('전체 조망 위치 상공 진입 완료')


# ── 뚜껑 조립 ──
def move_to_lid_pick_position(robot, config):
    print('뚜껑 픽업 위치 상공 진입 완료')

def lower_to_lid_pick(robot, config):
    print('뚜껑 픽업 위치 하강 완료')

def grab_lid(robot, config):
    print('뚜껑 그리퍼 닫기 완료')

def raise_from_lid_pick(robot, config):
    print('뚜껑 픽업 위치 상승 완료')

def move_to_lid_place_position(robot, config):
    print('뚜껑 삽입 위치 상공 진입 완료')

def lower_to_lid_place(robot, config):
    print('뚜껑 삽입 위치 하강 완료')

def release_lid(robot, config):
    print('뚜껑 그리퍼 해제 완료')

def raise_from_lid_place(robot, config):
    print('뚜껑 삽입 위치 상승 완료')


# ── 최종 게이트: 외관 이물질 검사 (완제품 전체 픽업/폐기) ──
def lower_for_pack_pickup(robot, config):
    print('완제품 픽업 위치 하강 완료')

def grab_pack(robot, config):
    print('완제품 그리퍼 닫기 완료')

def raise_for_pack_pickup(robot, config):
    print('완제품 픽업 위치 상승 완료')

def move_to_pack_discard_position(robot, config):
    print('완제품 폐기 위치 상공 진입 완료')

def lower_to_pack_discard(robot, config):
    print('완제품 폐기 위치 하강 완료')

def release_pack(robot, config):
    print('완제품 그리퍼 해제 완료')

def raise_from_pack_discard(robot, config):
    print('완제품 폐기 위치 상승 완료')


# ── 시퀀스 종료 ──
def return_home(robot, config):
    print('시퀀스 종료 후 홈 포지션 이동 완료')