'''
test_utils.py (unittest)

common/utils.py의 generate_grid()는 하드웨어와 무관한 순수 함수이므로
모킹 없이 직접 검증한다.

실행 방법:
    python -m unittest test_utils.py -v
'''

import unittest

from common.utils import generate_grid
from config import robot02_config


class TestGenerateGrid(unittest.TestCase):

    def test_slot_count_matches_grid_x_times_grid_y(self):
        for cnt, params in robot02_config.CELL_STORAGE_GRID_PARAMS.items():
            with self.subTest(cnt=cnt):
                coords = generate_grid(**params)
                self.assertEqual(len(coords), params["grid_x"] * params["grid_y"])

    def test_each_slot_has_top_and_bottom_with_6_elements(self):
        params = robot02_config.CELL_STORAGE_GRID_PARAMS[6]
        coords = generate_grid(**params)
        for slot in coords:
            self.assertIn("top", slot)
            self.assertIn("bottom", slot)
            self.assertEqual(len(slot["top"]), 6)
            self.assertEqual(len(slot["bottom"]), 6)

    def test_bottom_is_lower_than_top_by_offset_z(self):
        base = [0.0, 0.0, 0.10, 0.0, 0.0, 0.0]
        coords = generate_grid(base=base, grid_x=1, grid_y=1,
                                offset_x=0.03, offset_y=0.03, offset_z=0.05)
        slot = coords[0]
        self.assertAlmostEqual(slot["top"][2], 0.10)
        self.assertAlmostEqual(slot["bottom"][2], 0.05)   # 0.10 - 0.05

    def test_column_varies_faster_than_row(self):
        # grid_x=2, grid_y=2 배열에서 슬롯 순서가 (row0,col0)(row0,col1)(row1,col0)(row1,col1)인지 확인
        base = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        coords = generate_grid(base=base, grid_x=2, grid_y=2,
                                offset_x=0.03, offset_y=0.05, offset_z=0.02)
        xs = [round(c["top"][0], 5) for c in coords]
        ys = [round(c["top"][1], 5) for c in coords]

        self.assertEqual(xs, [0.0, 0.03, 0.0, 0.03])
        self.assertEqual(ys, [0.0, 0.0, 0.05, 0.05])

    def test_pose_values_are_preserved_from_base(self):
        base = [0.0, 0.0, 0.0, 180, 0, 90]
        coords = generate_grid(base=base, grid_x=2, grid_y=1,
                                offset_x=0.03, offset_y=0.03, offset_z=0.05)
        for slot in coords:
            self.assertEqual(slot["top"][3:], [180, 0, 90])
            self.assertEqual(slot["bottom"][3:], [180, 0, 90])

    def test_single_slot_grid(self):
        base = [1.0, 2.0, 3.0, 0, 0, 0]
        coords = generate_grid(base=base, grid_x=1, grid_y=1,
                                offset_x=0.03, offset_y=0.03, offset_z=0.05)
        self.assertEqual(len(coords), 1)
        self.assertEqual(coords[0]["top"], [1.0, 2.0, 3.0, 0, 0, 0])
        self.assertEqual(coords[0]["bottom"], [1.0, 2.0, 2.95, 0, 0, 0])


if __name__ == '__main__':
    unittest.main()
