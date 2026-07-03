'''
    좌표·그리드 파라미터·PLC2 접속 정보(포트 1025)등 설정
'''

# ── 통신 접속 정보 ──
ROBOT2_IP = "192.168.3.7"
ROBOT2_NAME = "NRMK-Indy7"
PLC2_CONNECTION = {"plc_ip": "192.168.3.130", "plc_port": 1025}
START_SIGNAL_ADDRESS = "Y24"

# ── 셀 보관함 / 삽입 슬롯 그리드 파라미터 (6구/8구 가변 대응) ──
# generate_grid(base, grid_x, grid_y, offset_x, offset_y, num_layers, layer_height)에 그대로 전달
CELL_STORAGE_GRID_PARAMS = {
    6: {"base": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "grid_x": 2, "grid_y": 3,
        "offset_x": 0.03, "offset_y": 0.03},
    8: {"base": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "grid_x": 2, "grid_y": 4,
        "offset_x": 0.03, "offset_y": 0.03},
}
CELL_INSERT_GRID_PARAMS = {
    6: {"base": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "grid_x": 2, "grid_y": 3,
        "offset_x": 0.03, "offset_y": 0.03},
    8: {"base": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "grid_x": 2, "grid_y": 4,
        "offset_x": 0.03, "offset_y": 0.03},
}

# ── 위치 좌표 [x, y, z, rx, ry, rz] (m, deg) ──
POLARITY_DISCARD_POSITION = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
LID_PICK_POSITION = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
LID_PLACE_POSITION = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
PACK_DISCARD_POSITION = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
FULL_VIEW_POSITION = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

# ── 위치별 2단 접근 오프셋(m) ──
CELL_PICK_RETRACT_Z = 0.03 # 배터리 셀 픽업 시 상공 오프셋
CELL_INSERT_RETRACT_Z = 0.03 # 배터리 셀 삽입 시 상공 오프셋
POLARITY_DISCARD_RETRACT_Z = 0.05 # 불량 배터리 폐기 시 상공 오프셋
LID_PICK_RETRACT_Z = 0.05 # 배터리 셀 덮개 픽업 시 상공 오프셋
LID_PLACE_RETRACT_Z = 0.05 # 배터리 셀 덮개 삽입 시 상공 오프셋
PACK_DISCARD_RETRACT_Z = 0.08 # 완제품 폐기 시 상공 오프셋
PACK_PICKUP_RETRACT_Z = 0.08   # 완제품(거치대 고정 위치) 픽업용

# ── 속도 파라미터 ──
APPROACH_VEL_LEVEL = 5     # 상공 이동(자유 공간)
PRECISION_VEL_LEVEL = 2    # 하강/접근/삽입(대상물 근접)
ROTATION_VEL_LEVEL = 2     # 회전 이동

# ── 그리퍼 ──
GRIPPER_DO_INDEX = 0 # set_do()에 사용되는 디지털 출력 채널 번호