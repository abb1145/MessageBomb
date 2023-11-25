import pynput  # 使用pynput控制键盘
import time

controller = pynput.keyboard.Controller()


def count_down():  # 倒计时
    for i in range(5, 0, -1):
        print(i)
        time.sleep(1)


def send_message(text: str, f: int, lag: float = 0.1):  # 发送消息
    for i in range(0, f):
        for j in text:
            with controller.pressed(j):
                pass
        with controller.pressed(pynput.keyboard.Key.enter):
            pass
        time.sleep(lag)
