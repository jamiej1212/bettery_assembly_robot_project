#=================================================
#   순수 좌표 계산
#=================================================

'''
    기준 좌표와 배열 파라미터로 그리드 전체 좌표 리스트를 계산
    로봇2의 셀 보관함(6구/8구)·셀 삽입 슬롯 좌표 산출용
    AI팀이 넘기는 정수 인덱스를 절대 좌표로 환산

    base: [x, y, z, rx, ry, rz] -> x와 y가 가장 작은 좌표
    반환:
    [{
        'top': [x, y, z, rx, ry, rz],
        'bottom':[x, y, z, rx, ry, rz]
    },
    {
        'top': [x, y, z, rx, ry, rz],
        'bottom':[x, y, z, rx, ry, rz]
    },...]

'''
def generate_grid(base, grid_x, grid_y, offset_x, offset_y, offset_z):
    coords = []
    for row in range(grid_y):
        y = base[1] + row * offset_y
        for col in range(grid_x):
            x = base[0] + col * offset_x
            bottom_z = base[2] - offset_z
            coords.append({
                'top': ([x, y] + list(base[2:])),
                'bottom': ([x, y, bottom_z] + list(base[3:]))
            })
    
    print('[INFO] 그리드 좌표 계산 완료')
    return coords
