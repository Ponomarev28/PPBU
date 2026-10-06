from tkinter import *

def answer(event):
    answ = num.get().strip()
    result.configure(text=answ)
root = Tk()
root.title('Start')
WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()
X = 300
Y = 100
# root.geometry('300x100+400+200')
root.geometry(f'{X}x{Y}+{WIDTH // 2 - X // 2}+{HEIGHT // 2 - Y // 2 - 25}')

promt = Label(text='Введите значение', font='Arial 12')
promt.pack()
# promt.pack(side=BOTTOM)
num = Entry(width=5, font='Arial 15', justify='center')
num.pack()
num.pack()

result = Label(text="   ", font='Arial 15', bg='lightgray')
result.pack(pady=10)

num.bind('<Return>', answer)

root.mainloop()