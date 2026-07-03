# ============================================
# 전역 비상정지 — PLC 기반, 로봇1·2 동시, 초기 상태로 리셋
# ============================================
class EmergencyStopHandler:
    '''
        비상정지 비트를 별도 스레드에서 상시 폴링하다
        ON 전환 감지 시 robot.pause() 호출
    '''
    def watch_emergency_signal(plc, robot, address):
        print('a')

    def stop_watching(): #감시 스레드를 종료
        print('감시 스레드 종료')