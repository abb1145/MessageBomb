import tkinter as tk
import message as message

# 创建主窗口
root = tk.Tk()
root.title("MESSAGE BOMB!!!!!!")
root.geometry("450x300")
root.resizable(False, False)

# 初始化变量
text = tk.StringVar()
frequency = tk.IntVar()
lag = tk.DoubleVar()

lag.set(0.1)  # lag赋值0.1


def send():
    send_task()


def send_task():
    message.count_down()
    # !!!!!attack it!!!!!
    message.send_message(text.get(), frequency.get(), lag.get())


tk.Label(root, text="message text: ").place(x=50, y=80)
tk.Label(root, text="send frequency: ").place(x=50, y=120)
tk.Label(root, text="lag time: ").place(x=50, y=160)

# 输入框
# 输入发送内容
entry_text = tk.Entry(root, textvariable=text)  # type: ignore
entry_text.place(x=155, y=80)

# 输入发送次数
entry_f = tk.Entry(root, textvariable=frequency)  # type: ignore
entry_f.place(x=155, y=120)

# 输入发送间隔
entry_lag = tk.Entry(root, textvariable=lag)  # type: ignore
entry_lag.place(x=155, y=160)

# 发送按钮
btn_send = tk.Button(root, text="!!ATTACK!!", command=send)
btn_send.place(x=160, y=210)


root.mainloop()
