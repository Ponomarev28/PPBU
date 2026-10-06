from tkinter import *
from tkinter import messagebox as mb


def summ():
    s1 = e1.get()
    if not s1.lstrip('-').isdigit():
        mb.showerror('Ошибка', 'В первом поле должно быть целое число')
        return
    s2 = e2.get()
    if not s2.lstrip('-').isdigit():
        mb.showerror('Ошибка', 'Во втором поле должно быть целое число')
        return
    s3 = e3.get()
    if not s3.lstrip('-').isdigit():
        mb.showerror('Ошибка', 'В третьем поле должно быть целое число')
        return


    int_1 = int(s1)
    int_2 = int(s2)
    int_3 = int(s3)
    summa = int_1 + int_2 + int_3
    m1['text'] = f'{s1} + {s2} + {s3} = {summa}'


def mult():
    s1 = e1.get()
    if not s1.lstrip('-').isdigit():
        mb.showerror('Ошибка', 'В первом поле должно быть целое число')
        return
    s2 = e2.get()
    if not s2.lstrip('-').isdigit():
        mb.showerror('Ошибка', 'Во втором поле должно быть целое число')
        return
    s3 = e3.get()
    if not s3.lstrip('-').isdigit():
        mb.showerror('Ошибка', 'В третьем поле должно быть целое число')
        return


    int_1 = int(s1)
    int_2 = int(s2)
    int_3 = int(s3)
    multip = int_1 * int_2 * int_3
    m1['text'] = f'{s1} * {s2} * {s3} = {multip}'

    # answer = mb.askretrycancel(title='Вопрос', message='Сложить еще 3 числа?')
    # if answer:
    #     e1.delete(0, END)
    #     e2.delete(0, END)
    #     e3.delete(0, END)
    #     m1['text'] = ''
    # else:
    #     window.destroy()

window = Tk()
window.title("Калькулятор")
m = Label(height = 3, text='Введите три числа и нажмите кнопку для вычисления суммы или произведения')
m.pack()
e1 = Entry()
e1.pack()
e2 = Entry()
e2.pack()
e3 = Entry()
e3.pack()
b1 = Button(text='Сложить три числа', command=summ)
b1.pack()
b2 = Button(text='Умножить три числа', command=mult)
b2.pack()
m1 = Label(height = 3)
m1.pack()

window.mainloop()
