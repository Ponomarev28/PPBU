from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import requests


def load_cryptocurrencies():
    response = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1')
    response.raise_for_status()
    data = response.json()
    return data


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
