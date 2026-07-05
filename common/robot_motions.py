# common/robot_motion.py
import time
from common.networks import RobotInterface
from common.utils import generate_grid

class RobotClient(RobotInterface):
    def __init__(self, config):
        super().__init__(config.ROBOT_IP, config.ROBOT_NAME)
        self.config = config
        self._is_paused = False

    def _check_move_done(self) -> None:
        while True:
            if self.indy.get_robot_status()['movedone'] == 1:
                break
            time.sleep(0.1)

    def move_to(self, pos, level: int) -> None:
        if isinstance(pos, str):
            target_pos = getattr(self.config, pos)
        elif isinstance(pos, (list, tuple)):
            target_pos = pos
        else:
            raise ValueError(f'move_to()의 pos는 config 좌표명(str) 또는 좌표 리스트/튜플이어야 합니다.'
                f'받은 값: {pos!r} ({type(pos).__name__})')
        
        self.indy.set_task_vel_level(level)
        self.indy.task_move_to(target_pos)
        self._check_move_done()
        
    def grab(self) -> None:
        self.indy.set_do(self.config.GRIPPER_DO_INDEX, True)
        time.sleep(self.config.GRIPPER_DO_SLEEP)

    def release(self) -> None:
        self.indy.set_do(self.config.GRIPPER_DO_INDEX, False)
        time.sleep(self.config.GRIPPER_DO_SLEEP)

    def return_home(self) -> None:
        self.indy.go_home()
        self._check_move_done()

    def pause(self) -> None:
        if self._is_paused:
            return
        self.indy.stop_motion()
        self._is_paused = True
    
    @property
    def is_paused(self) -> bool:
        return self._is_paused
    
    def resume(self) -> None:
        if not self._is_paused:
            return
        self._is_paused = False

    def emergency_stop(self) -> None:
        self.indy.stop_emergency()

    def reset_emergency(self) -> None:
        self.indy.reset_robot()

    def get_coords(self, index, cnt) -> list:
        grid_list = ['CELL_STORAGE_GRID_PARAMS', 'CELL_INSERT_GRID_PARAMS', 'CELL_DISCARD_GRID_PARAMS']
        target_grid = grid_list[index]
        grid_params = getattr(self.config, target_grid)[cnt]
        coords = generate_grid(**grid_params)
        return coords
        
