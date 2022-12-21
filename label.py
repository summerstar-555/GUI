from tkinter import *
top = Tk()
top.geometry("480x200")
top.title('label')
label = Label(top, text='hello GUI!', width=100, height=50,
              background='white', foreground='black',
              font=(' ', 12))
label.pack()
top.mainloop()
