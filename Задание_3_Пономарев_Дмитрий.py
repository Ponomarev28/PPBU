from tkinter import *
from tkinter import messagebox as mb


def calculate(operation):
    """Сделал общую функцию, которая принимает метку operation и осуществляет соответствующее вычисление"""
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

    if operation == '+':
        result = int_1 + int_2 + int_3
        m1['text'] = f'{s1} + {s2} + {s3} = {result}'
    elif operation == '*':
        result = int_1 * int_2 * int_3
        m1['text'] = f'{s1} * {s2} * {s3} = {result}'


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
b1 = Button(text='Сложить три числа', command=lambda: calculate('+'))
b1.pack()
b2 = Button(text='Умножить три числа', command=lambda: calculate('*'))
b2.pack()
m1 = Label(height = 3)
m1.pack()

window.mainloop()
