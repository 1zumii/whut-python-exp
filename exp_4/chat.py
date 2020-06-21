import tkinter
from tkinter import *
import time

# 创建窗口
root = Tk()
root.title("ergou")


# root.geometry("650x750")

# 定义发送消息函数
def msgsend():
	msg = '我' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + '\n'
	msg_list.insert(END, msg, 'green')  # 添加时间
	msg_list.insert(END, sen_msg.get('0.0', END))  # 获取发送消息，添加文本到消息列表
	sen_msg.delete('0.0', END)  # 清空发送消息


# 定义取消发送消息函数
def cancel():
	msg_list.delete('0.0', END)  # 取消发送消息，即清空发送消息


# 定义大框架
f_msg = tkinter.Frame(width=300, height=300)
msg_sen = tkinter.Frame(width=300, height=300)
f_bottom = tkinter.Frame(width=300, height=100)
f_img = tkinter.Frame(width=100, height=700)

# 添加到主窗口
f_msg.pack()
msg_sen.pack()
f_bottom.pack()
f_img.pack()

# 给框架里添加标签
msg_list = tkinter.Text(f_msg)
msg_list.tag_config('green', foreground='blue')

sen_msg = tkinter.Text(msg_sen)
bt_send = tkinter.Button(f_bottom, text='send', command=msgsend)
bt_cancel = tkinter.Button(f_bottom, text='cancel', command=cancel)

msg_list.grid()
sen_msg.grid()
bt_send.grid(row=0, column=0)
bt_cancel.grid(row=0, column=1)
# img.grid()
# img2.grid(ipady=8)

root.mainloop()
