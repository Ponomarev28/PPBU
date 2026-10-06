from tkinter import *

# def change():
#     metka['text'] = 'Черная метка'
#     metka['bg'] = 'black'
#
# window = Tk()
# metka = Label(text="Привет всем!", bg="Salmon", fg="FireBrick",
#               width=15, height=5)
# metka.pack()
# knopka = Button(text='Изменить метку', width=15, height=3)
# knopka.config(command=change)
# knopka.pack()
# window.mainloop()
''' смайлики'''
# a = 128512
# def change():
#     global a
#     a += 1
#     metka['text'] = chr(a)

''' центрирование меток'''
#
# window = Tk()
# metka = Label(text=chr(a), font='Arial 64')
# metka.pack()
# knopka = Button(text='Следующий смайлик', width=30, height=3)
# knopka.config(command=change)
# knopka.pack()
# window.mainloop()

# window = Tk()
# frame_top = Frame(window)
# frame_bottom = Frame(window)
# frame_top.pack()
# frame_bottom.pack()
#
# metka1 = Label(frame_top, text='Метка 1', bg='red')
# metka1.pack(side=LEFT)
# metka2 = Label(frame_top, text='Метка 2', bg='yellow')
# metka2.pack(side=LEFT)
# metka3 = Label(frame_top, text='Метка 3', bg='green')
# metka3.pack(side=LEFT)
# metka4 = Label(frame_bottom, text='Метка 4', bg='blue')
# metka4.pack(side=LEFT)
# metka5 = Label(frame_bottom, text='Метка 5', bg='gray')
# metka5.pack(side=LEFT)
# metka6 = Label(frame_bottom, text='Метка 6', bg='salmon')
# metka6.pack(side=LEFT)
#
# window.mainloop()

''' ввод '''

# def read():
#     name = e.get()
#     print(name)
#     e.delete(0, END)
#
# def read2():
#     city = e2.get()
#     print(city)
#     e2.delete(0, END)
#
# window = Tk()
# f1 = Frame()
# f1.pack()
# f2 = Frame()
# f2.pack()
#
# m = Label(f1, text='Введите имя:', bg='gray', fg='white', font='Courier 18 bold')
# m.pack(side=LEFT)
# e = Entry(f1, width=50, bg='gray', fg='white', font='Courier 18 bold')
# e.pack(side=LEFT)
# b = Button(f1, text='Ввод', bg='gray', fg='white', font='Courier 18 bold', command=read)
# b.pack(side=LEFT)
#
# m2 = Label(f2, text='Введите город:', bg='gray', fg='white', font='Courier 18 bold')
# m2.pack(side=LEFT)
# e2 = Entry(f2, width=50, bg='gray', fg='white', font='Courier 18 bold')
# e2.pack(side=LEFT)
# b2 = Button(f2, text='Ввод', bg='gray', fg='white', font='Courier 18 bold', command=read2)
# b2.pack(side=LEFT)
#
# window.mainloop()

''' многострочный ввод '''

def read():
    t = text.get(1.0, END)
    print(t)
def

window = Tk()
text = Text(width=30, height=8, bg='black', fg='white')
text.pack(side=LEFT)
scroll = Scrollbar(command=text.yview)
scroll.pack(side=LEFT, fill=Y)
text.config(yscrollcommand=scroll.set)
b = Button(text='Ввод', command=read)
b.pack()

window.mainloop()