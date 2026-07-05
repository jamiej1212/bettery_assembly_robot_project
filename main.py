'''
    로봇팀 단독 테스트용
'''
'''
    from common.robot_motions import RobotClient
    from config import robot01_config, robot02_config, plc_config
    from common.networks import PLCInterface


    def main():
        print("메인 프로그램이 실행되었습니다.")

        robot1 = RobotClient(robot01_config)
        robot2 = RobotClient(robot02_config)
        plc = PLCInterface(plc_config.PLC_IP, plc_config.PLC_PORT)

        robot1.connect()
        robot2.connect()
        plc.connect()

        try:
            robot1.move_to('CV_TOP', 5)
        except Exception as e:
            print(e)
        finally:
            robot1.disconnect()
            robot2.disconnect()
            plc.close()


    if __name__ == '__main__':
        main()
'''

'''
    robot_motions.py 단독 검증용 테스트 스크립트
    PLC · AI팀 통신(PLCInterface, 신호 수신/송신)은 배제하고,
    RobotClient의 모션 프리미티브(move_to / grab / release / return_home)만 검증한다.

    [안전 수칙]
    - 최초 실행 시 반드시 저속(vel_level 2~3)으로 시작할 것
    - 로봇 작동 반경 내 인원·장애물이 없는지 확인 후 실행할 것
    - 좌표값(BC_TOP 등)이 아직 플레이스홀더([0,0,0,0,0,0])라면
      실제 로봇을 기동하지 말고 config 파일에 실측 좌표를 먼저 반영할 것
'''

import time

from common.robot_motions import RobotClient
from config import robot01_config, robot02_config


TEST_VEL_LEVEL = 2  # 저속 — 실기 검증 완료 전까지 임의로 올리지 말 것


def run_motion_test(robot: RobotClient, robot_label: str, top_pos: str,
                     bottom_pos: str, second_top_pos: str, second_bottom_pos: str) -> None:
    """
    로봇 1대에 대해 픽앤플레이스 4단 패턴(이동-그랩-이동-릴리즈)과
    홈 복귀를 순서대로 실행하며 각 단계 결과를 출력한다.

    top_pos/bottom_pos: 픽업 지점의 상공/하강 좌표명(config 내 속성명)
    second_top_pos/second_bottom_pos: 배치 지점의 상공/하강 좌표명
    """
    print(f"\n===== [{robot_label}] 모션 테스트 시작 =====")

    print(f"[{robot_label}] {top_pos} 이동")
    robot.move_to(top_pos, TEST_VEL_LEVEL)

    print(f"[{robot_label}] {bottom_pos} 하강")
    robot.move_to(bottom_pos, TEST_VEL_LEVEL)

    print(f"[{robot_label}] GRAB")
    robot.grab()

    print(f"[{robot_label}] {top_pos} 상승")
    robot.move_to(top_pos, TEST_VEL_LEVEL)

    print(f"[{robot_label}] {second_top_pos} 이동")
    robot.move_to(second_top_pos, TEST_VEL_LEVEL)

    print(f"[{robot_label}] {second_bottom_pos} 하강")
    robot.move_to(second_bottom_pos, TEST_VEL_LEVEL)

    print(f"[{robot_label}] RELEASE")
    robot.release()

    print(f"[{robot_label}] {second_top_pos} 상승")
    robot.move_to(second_top_pos, TEST_VEL_LEVEL)

    print(f"[{robot_label}] HOME 복귀")
    robot.return_home()

    print(f"===== [{robot_label}] 모션 테스트 종료 =====\n")


def main():
    robot1 = RobotClient(robot01_config)
    robot2 = RobotClient(robot02_config)

    robot1.connect()
    robot2.connect()

    try:
        # 로봇1: BC(베이스 보관) → CV(컨베이어) 경로
        run_motion_test(robot1, "로봇1",
                        top_pos='BC_TOP', bottom_pos='BC_BOTTOM',
                        second_top_pos='CV_TOP', second_bottom_pos='CV_BOTTOM')
        time.sleep(1)

        # 로봇2: 현재 config에 상공/하강 짝을 이루는 좌표가 정의되어 있지 않으므로
        # (POLARITY_DISCARD_POSITION 등은 단일 좌표), 뚜껑 픽업/조립 위치로 대체 검증.
        # 단일 좌표만 반복 검증하고자 하면 아래 두 줄만 남기고 호출부를 단순화해도 무방함.
        run_motion_test(robot2, "로봇2",
                        top_pos='LID_PICK_POSITION', bottom_pos='LID_PICK_POSITION',
                        second_top_pos='LID_PLACE_POSITION', second_bottom_pos='LID_PLACE_POSITION')

    except Exception as e:
        print(f"[오류] 모션 테스트 중 예외 발생: {e}")

    finally:
        robot1.disconnect()
        robot2.disconnect()


if __name__ == '__main__':
    main()