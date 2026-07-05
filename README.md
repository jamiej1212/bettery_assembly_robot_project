### config 수정하지 말 것!!!

## main.py에서 할 일

### 1. import 하기

```
from common.robot_motions import RobotClient
from config import robot01_config, robot02_config, plc_config
from common.networks import PLCInterface
```

### 2. robot01_config, robot02_config 넣고 RobotClient class 객체 robot1, robot2 만들기

```
robot1 = RobotClient(robot01_config)
robot2 = RobotClient(robot02_config)
```

### 3. PLCInterface 객체 만들기

```
plc = PLCInterface(plc_config.PLC_IP, plc_config.PLC_PORT)
```

### 4. robot1, robot2 실제 로봇이랑 연결하기

```
robot1.connect()
robot2.connect()
```

### 5. PLC 연결하기

```
plc.connect()
```

### 6. class 함수 사용해서 로봇 제어하기(PLC 신호/비전 센서 결과)

- move_to(좌표명(하단 참조) 또는 좌표 list, 속도 레벨(1~9))
  | robot1 | robot2 |
  |---|---|
  | `BC_TOP` / `BC_BOTTOM` | `CV_TOP` / `CV_BOTTOM` |
  | `CV_TOP` / `CV_BOTTOM` | `LC_TOP` / `LC_BOTTOM` |
  | `DD_TOP` / `DD_BOTTOM` | `LD_TOP` / `LD_BOTTOM` |
  | | `DD_TOP` / `DD_BOTTOM` |
- grab()
- release()
- return_home()

### 7. robot2 그리드 좌표 계산하기

```
cc_coords = robot2.get_coords(컨테이너 타입, 삽입구 개수)
```

| 값  | 의미         |
| --- | ------------ |
| `0` | 셀 컨테이너  |
| `1` | 배터리팩     |
| `2` | 셀 폐기 라인 |

- 반환값 활용 방법
  ex) 첫 번째 배터리 셀 top 위치로 이동

```
robot2.move_to(cc_coords[0]['top'], 속도)
```

### 8. 일시 정지 후 다시 동작 이어갈 때

```
robot1.pause()
# 손 치우기
robot1.resume()
robot1.move_to(마지막 이동 좌표, 속도 레벨)
```

### 9. 로직 끝나면 다 닫아주기

```
robot1.disconnect()
robot2.disconnect()
plc.close()
```

- plc 비상 정지 신호 발생 시(emergency_stop과 reset_emergency는 한 세트)

```
robot1.emergency_stop()
robot2.emergency_stop()

robot1.reset_emergency()
robot2.reset_emergency()
```
