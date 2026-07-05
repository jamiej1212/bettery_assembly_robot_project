# common/robot_motion.py
import time
from common.networks import RobotInterface

class RobotClient(RobotInterface):
    def __init__(self, config):
        super().__init__(config.ROBOT_IP, config.ROBOT_NAME)
        self.config = config

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