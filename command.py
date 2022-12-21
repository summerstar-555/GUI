from tkinter import *
top = Tk()  # Tk方法返回一个根窗口
top.geometry("400x250")
top.title('command')

"""
bt = Button(top, height=2,
           width=6, text='Quit', bg="black", fg='white', font=('黑体', 20, 'bold'),
           activeforeground='black', activebackground='yellow', command=top.quit)
创建一个按钮，高为6，宽为30，文本内容为hello world，黑色背景，白色黑体字体
大小20，点击按钮，背景变红，字体变绿，松开按钮后图形界面退出
"""
bt = Button(top, width=10, height=1, text='command')
bt.place(relx=0.5, rely=0.5, anchor=CENTER)
# bt.pack(side=LEFT, padx=100, pady=20)       # 设置按钮位置
top.mainloop()
