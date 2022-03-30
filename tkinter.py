from tkinter import *


def cBtn():
    lbl.config(text=end.get())



win = Tk()
win.geometry('300x350')
win.title("Led")
lbl = Label(win, text='Введите желаемый диаметр лампы', font=("Lucida Console", 20))
ent = Entry(win, width=8, font=("Lucida Console", 20))
lbl2 = Label(win, text='Введите кол-во светодиодов на метр', font=("Lucida Console", 20))
com = Combobox(winб , font=("Lucida Console", 20))
com['values'] = (30, 60, 120, 144)
btn = Button(win, text="Расчет", font=("Lucida Console", 30), command=cBtn)
lbl3 = Label(win, text='', font=("Lucida Console", 20))

lbl.pack(side=TOP)
lbl2.pack(side=TOP)
lbl3.pack(side=TOP)
btn.pack(side=TOP)
ent.pack(side=TOP)
com.pack(side=TOP)

win.mainloop()