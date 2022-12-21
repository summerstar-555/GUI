from tkinter import *

top = Tk()  # top方法返回一个根窗口
w = Button(top, height=6,
           width=30, text='Hello World!', bg="black", fg='white', font=('黑体', 20, 'bold'),
           activeforeground='black', activebackground='yellow', command=top.quit)
"""
创建一个按钮，高为6，宽为30，文本内容为hello world，黑色背景，白色黑体字体
大小20，点击按钮，背景变红，字体变绿，松开按钮后图形界面退出
"""
w.pack()
top.mainloop()
