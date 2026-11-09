from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import requests

root = Tk()
root.title('Курсы криптовалют к USD')
root.geometry('360x120')

Label(root, text='Криптовалюта').pack(padx=10)
target_combobox = ttk.Combobox(root, values=list(currencies.keys()))
target_combobox.pack(pady=3, padx=10)
target_combobox.bind('<<ComboboxSelected>>', update_currency_label)

target_label = ttk.Label()
target_label.pack()

Button(text='Получить курс', command=exchange).pack(pady=10, padx=10)

root.mainloop()
