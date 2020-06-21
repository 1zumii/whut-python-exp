import tkinter as tk
import tkinter.messagebox
import pickle

root = tkinter.Tk()
root.geometry('400x300')
root.title("武理工欢迎你！")

# 画布
canvas = tkinter.Canvas(root, width=400, height=300)
pic = tkinter.PhotoImage(file='1.png')
image = canvas.create_image(0, 0, anchor='nw', image=pic)
canvas.pack(side='top')

# 登录界面，用户、密码
label1 = tkinter.Label(root, text='账号：')
label1.place(x=80, y=80)
label2 = tkinter.Label(root, text='密码：')
label2.place(x=80, y=120)

var_usr_name = tkinter.StringVar()
entry_usr_name = tkinter.Entry(root, textvariable=var_usr_name)
entry_usr_name.place(x=130, y=80)

var_usr_pwd = tkinter.StringVar()
entry_usr_pwd = tkinter.Entry(root, textvariable=var_usr_pwd, show='*')
entry_usr_pwd.place(x=130, y=120)


def usr_log_in():
	usr_name = var_usr_name.get()
	user_pwd = var_usr_pwd.get()
	# 从本地字典获取用户信息，如果没有则新建本地数据库
	try:
		with open('usr_info.pickle', 'rb') as usr_file:
			usrs_info = pickle.load(usr_file)
	except FileNotFoundError:
		with open('usr_info.pickle', 'wb') as usr_file:
			usrs_info = {'admin': 'admin'}
			pickle.dump(usrs_info, usr_file)
	if usr_name in usrs_info:
		if user_pwd in usrs_info[usr_name]:
			tkinter.messagebox.showinfo(title='welcome', message=usr_name + '欢迎登录')
		else:
			tkinter.messagebox.showerror(title='tip', message='密码错误,请重新输入！')
	elif usr_name == '' or user_pwd == '':
		tkinter.messagebox.showerror(title='tip', message='用户名或密码为空！')
	else:
		go_signup = tkinter.messagebox.askyesno('欢迎', '你还没注册，是否现在去注册？')
		if go_signup:
			usr_sign_up()


def usr_sign_up():
	# 确认注册时的相应函数
	def signtowcg():
		# 获取输入框内的内容
		nn = new_name.get()
		np = new_pwd.get()
		npf = new_pwd_confirm.get()

		# 本地加载已有用户信息,如果没有则已有用户信息为空
		try:
			with open('usr_info.pickle', 'rb') as usr_file:
				exist_usr_info = pickle.load(usr_file)
		except FileNotFoundError:
			exist_usr_info = {}

		# 检查用户名存在、密码为空、密码前后不一致
		if nn in exist_usr_info:
			tk.messagebox.showerror('错误', '用户名已存在')
		elif np == '' or nn == '':
			tk.messagebox.showerror('错误', '用户名或密码为空')
		elif np != npf:
			tk.messagebox.showerror('错误', '密码前后不一致')

		# 注册信息没有问题则将用户名密码写入数据库
		else:
			exist_usr_info[nn] = np
			with open('usr_info.pickle', 'wb') as usr_file:
				pickle.dump(exist_usr_info, usr_file)
			tk.messagebox.showinfo('欢迎', '注册成功')
			# 注册成功关闭注册框
			window_sign_up.destroy()

	# 新建注册界面
	window_sign_up = tk.Toplevel(root)
	window_sign_up.geometry('350x200')
	window_sign_up.title('注册')
	# 用户名变量及标签、输入框
	new_name = tk.StringVar()
	tk.Label(window_sign_up, text='用户名：').place(x=10, y=10)
	tk.Entry(window_sign_up, textvariable=new_name).place(x=150, y=10)

	# 密码变量及标签、输入框
	new_pwd = tk.StringVar()
	tk.Label(window_sign_up, text='请输入密码：').place(x=10, y=50)
	tk.Entry(window_sign_up, textvariable=new_pwd, show='*').place(x=150, y=50)

	# 重复密码变量及标签、输入框
	new_pwd_confirm = tk.StringVar()
	tk.Label(window_sign_up, text='请再次输入密码：').place(x=10, y=90)
	tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*').place(x=150, y=90)

	# 确认注册按钮及位置
	bt_confirm_sign_up = tk.Button(
		window_sign_up, text='确认注册', command=signtowcg
	)
	bt_confirm_sign_up.place(x=150, y=130)


def usr_sign_quit():
	root.destroy()


# 按钮,登录、注册、退出
bt_login = tkinter.Button(root, text="登录", command=usr_log_in)
bt_login.place(x=80, y=220)
bt_sign_up = tkinter.Button(root, text="注册", command=usr_sign_up)
bt_sign_up.place(x=160, y=220)
bt_sign_quit = tkinter.Button(root, text="退出", command=usr_sign_quit)
bt_sign_quit.place(x=240, y=220)

root.mainloop()
