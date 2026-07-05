'''
    좌표·그리드 파라미터 등 설정
'''

# ── 통신 접속 정보 ──
ROBOT_IP = "192.168.3.5"
ROBOT_NAME = "NRMK-Indy7"

# ── 셀 보관함 / 삽입 슬롯 그리드 파라미터 (6구/8구 가변 대응) ──
# generate_grid(base, grid_x, grid_y, offset_x, offset_y, num_layers, layer_height)에 그대로 전달
CELL_STORAGE_GRID_PARAMS = {
    6: {"base": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "grid_x": 2, "grid_y": 3,
        "offset_x": 0.03, "offset_y": 0.03, "offset_z": 0.05},
    8: {"base": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "grid_x": 2, "grid_y": 4,
        "offset_x": 0.03, "offset_y": 0.03, "offset_z": 0.05},
}
CELL_INSERT_GRID_PARAMS = {
    6: {"base": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "grid_x": 2, "grid_y": 3,
        "offset_x": 0.03, "offset_y": 0.03, "offset_z": 0.05},
    8: {"base": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "grid_x": 2, "grid_y": 4,
        "offset_x": 0.03, "offset_y": 0.03, "offset_z": 0.05},
}
CELL_DISCARD_GRID_PARAMS = {
    6: {"base": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "grid_x": 2, "grid_y": 3,
        "offset_x": 0.03, "offset_y": 0.03, "offset_z": 0.05},
    8: {"base": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "grid_x": 2, "grid_y": 4,
        "offset_x": 0.03, "offset_y": 0.03, "offset_z": 0.05},
}

# ── 위치 좌표 [x, y, z, rx, ry, rz] (m, deg) ──
'''
    CV: 컨베이어
    LC: 뚜껑 컨테이너
    LD: 뚜껑 폐기 라인
    DD: 배터리팩 전체 폐기 라인
'''
CV_TOP = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
CV_BOTTOM = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
LC_TOP = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
LC_BOTTOM = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
LD_TOP = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
LD_BOTTOM = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
DD_TOP = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
DD_BOTTOM = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

# ── 그리퍼 ──
GRIPPER_DO_INDEX = 2 # set_do()에 사용되는 디지털 출력 채널 번호
GRIPPER_DO_SLEEP = 0.5