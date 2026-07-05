'''
test_robot_motions.py (pytest)

common/robot_motions.py의 RobotClient를 벤더 SDK(IndyDCPClient) 모킹으로 검증한다.
실물 로봇·시뮬레이터 없이 실행 가능하다.

실행 방법:
    pytest test_robot_motions.py -v
'''

import pytest
from unittest.mock import MagicMock, patch

from common.robot_motions import RobotClient
from config import robot01_config, robot02_config


@pytest.fixture
def mock_indy():
    """
    common.networks가 참조하는 IndyDCPClient 자리를 MagicMock으로 대체한다.
    get_robot_status()는 항상 이동 완료(movedone=1)로 응답하여,
    RobotClient 내부의 완료 대기 폴링이 즉시 종료되도록 고정한다.
    """
    with patch('common.networks.IndyDCPClient') as MockIndyClass:
        instance = MagicMock()
        instance.connect.return_value = True
        instance.get_robot_status.return_value = {'movedone': 1}
        MockIndyClass.return_value = instance
        yield instance


@pytest.fixture
def robot1(mock_indy):
    r = RobotClient(robot01_config)
    r.connect()
    return r


@pytest.fixture
def robot2(mock_indy):
    r = RobotClient(robot02_config)
    r.connect()
    return r


# ────────────────────────────────
# move_to
# ────────────────────────────────

def test_move_to_with_position_name_looks_up_config(robot1, mock_indy):
    robot1.move_to('BC_TOP', 3)
    mock_indy.set_task_vel_level.assert_called_once_with(3)
    mock_indy.task_move_to.assert_called_once_with(robot01_config.BC_TOP)


def test_move_to_with_raw_coordinates_passes_through(robot1, mock_indy):
    custom_pos = [0.1, 0.2, 0.3, 0, 0, 0]
    robot1.move_to(custom_pos, 5)
    mock_indy.task_move_to.assert_called_once_with(custom_pos)


def test_move_to_invalid_type_raises_value_error(robot1):
    with pytest.raises(ValueError):
        robot1.move_to(123, 3)   # 문자열도 리스트/튜플도 아닌 값


def test_move_to_unknown_position_name_raises_attribute_error(robot1):
    with pytest.raises(AttributeError):
        robot1.move_to('NOT_A_REAL_POSITION', 3)   # config에 없는 이름


def test_check_move_done_polls_until_movedone(mock_indy):
    # 1,2회차는 미완료 -> 3회차에 완료
    mock_indy.get_robot_status.side_effect = [
        {'movedone': 0},
        {'movedone': 0},
        {'movedone': 1},
    ]
    r = RobotClient(robot01_config)
    r.connect()
    r.move_to('CV_TOP', 3)
    assert mock_indy.get_robot_status.call_count == 3


# ────────────────────────────────
# grab / release
# ────────────────────────────────

def test_grab_sets_gripper_do_true(robot1, mock_indy):
    robot1.grab()
    mock_indy.set_do.assert_called_once_with(robot01_config.GRIPPER_DO_INDEX, True)


def test_release_sets_gripper_do_false(robot1, mock_indy):
    robot1.release()
    mock_indy.set_do.assert_called_once_with(robot01_config.GRIPPER_DO_INDEX, False)


# ────────────────────────────────
# return_home / emergency_stop
# ────────────────────────────────

def test_return_home_calls_go_home_and_waits(robot1, mock_indy):
    robot1.return_home()
    mock_indy.go_home.assert_called_once()
    mock_indy.get_robot_status.assert_called()   # 완료 대기 폴링 발생 확인


def test_emergency_stop_calls_indy_stop_emergency(robot1, mock_indy):
    robot1.emergency_stop()
    mock_indy.stop_emergency.assert_called_once()


def test_reset_emergency_calls_indy_reset_robot(robot1, mock_indy):
    robot1.reset_emergency()
    mock_indy.reset_robot.assert_called_once()


def test_emergency_stop_then_reset_emergency_are_independent_calls(robot1, mock_indy):
    """
    emergency_stop()과 reset_emergency()가 서로 다른 벤더 커맨드를 호출하며,
    한쪽 호출이 다른 쪽 mock을 오염시키지 않는지 확인한다.
    """
    robot1.emergency_stop()
    robot1.reset_emergency()

    mock_indy.stop_emergency.assert_called_once()
    mock_indy.reset_robot.assert_called_once()
    mock_indy.stop_motion.assert_not_called()   # pause()의 stop_motion()과 혼동되지 않는지 확인


# ────────────────────────────────
# pause / resume — 멱등성 검증
# ────────────────────────────────

def test_pause_calls_stop_motion_once(robot1, mock_indy):
    robot1.pause()
    mock_indy.stop_motion.assert_called_once()
    assert robot1.is_paused is True


def test_pause_called_repeatedly_only_hits_vendor_sdk_once(robot1, mock_indy):
    """
    PLC 감시 루프가 정지 신호가 켜져 있는 동안 매 폴링마다 pause()를
    반복 호출하더라도, 벤더 SDK 호출은 최초 1회로 제한되어야 한다.
    """
    for _ in range(5):
        robot1.pause()
    mock_indy.stop_motion.assert_called_once()


def test_resume_clears_paused_flag(robot1, mock_indy):
    robot1.pause()
    robot1.resume()
    assert robot1.is_paused is False


def test_resume_without_prior_pause_does_nothing(robot1):
    robot1.resume()   # pause() 없이 곧바로 호출
    assert robot1.is_paused is False


def test_resume_called_repeatedly_is_safe(robot1, mock_indy):
    robot1.pause()
    robot1.resume()
    robot1.resume()   # 중복 호출
    assert robot1.is_paused is False


def test_pause_after_resume_can_pause_again(robot1, mock_indy):
    """정지 -> 재개 -> 재정지 사이클이 매번 벤더 SDK에 정확히 반영되는지 확인."""
    robot1.pause()
    robot1.resume()
    robot1.pause()
    assert mock_indy.stop_motion.call_count == 2
    assert robot1.is_paused is True


# ────────────────────────────────
# get_coords — 그리드 좌표 조회
# ────────────────────────────────

@pytest.mark.parametrize("index, expected_key", [
    (0, "CELL_STORAGE_GRID_PARAMS"),
    (1, "CELL_INSERT_GRID_PARAMS"),
    (2, "CELL_DISCARD_GRID_PARAMS"),
])
def test_get_coords_selects_correct_grid(robot2, index, expected_key):
    expected_params = getattr(robot02_config, expected_key)[6]
    coords = robot2.get_coords(index, 6)

    # generate_grid 결과의 슬롯 수가 grid_x * grid_y와 일치하는지로 올바른 그리드가
    # 선택되었는지 간접 검증
    assert len(coords) == expected_params["grid_x"] * expected_params["grid_y"]


def test_get_coords_slot_has_top_and_bottom(robot2):
    coords = robot2.get_coords(0, 6)
    for slot in coords:
        assert "top" in slot and "bottom" in slot
        assert len(slot["top"]) == 6
        assert len(slot["bottom"]) == 6


def test_get_coords_invalid_index_raises_index_error(robot2):
    with pytest.raises(IndexError):
        robot2.get_coords(99, 6)


def test_get_coords_invalid_cnt_raises_key_error(robot2):
    with pytest.raises(KeyError):
        robot2.get_coords(0, 7)   # 6/8 이외의 값
