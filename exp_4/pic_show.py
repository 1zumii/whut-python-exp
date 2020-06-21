from PIL import Image
import tkinter
import tkinter.filedialog
import tkinter.messagebox


class Window:
	def __init__(self):
		self.root = root = tkinter.Tk()

		self.label = tkinter.Label(root, text='选择图片文件:')
		self.label.place(x=5, y=15)
		self.entryFile = tkinter.Entry(root)
		self.entryFile.place(x=10, y=55, width=200)
		self.BrowserFileButton = tkinter.Button(root, text='浏览', command=self.BrowserFile)
		self.BrowserFileButton.place(x=235, y=50)

		self.ButtonCov = tkinter.Button(root, text='展示图片', command=self.showPic)
		self.ButtonCov.place(x=110, y=180)

	def BrowserFile(self):
		file = tkinter.filedialog.askopenfilename(
			title='Python player',
			filetypes=[
				('JPG', '*.jpg'), ('BMP', '*.bmp'),
				('GIF', '*.gif'), ('PNG', '*.png')
			]
		)
		if file:
			self.entryFile.delete(0, tkinter.END)
			self.entryFile.insert(tkinter.END, file)

	def showPic(self):
		image_path = self.entryFile.get()
		print(image_path)
		image = Image.open(image_path)
		image.show()

	def mainloop(self):
		self.root.minsize(280, 270)
		self.root.maxsize(280, 250)
		self.root.title('图片展示')
		self.root.mainloop()


if __name__ == "__main__":
	window = Window()
	window.mainloop()
