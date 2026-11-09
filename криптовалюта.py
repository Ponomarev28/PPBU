from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import requests


def load_cryptocurrencies():
    response = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1')
    response.raise_for_status()
    data = response.json()
    return data

def update_currency_label(event):
    code = target_combobox.get()
    name = currencies[code]['name']
    target_label.config(text=name)


def exchange():
    target_symbol = target_combobox.get().strip().upper()
    if target_symbol in currencies:
        target_code = currencies[target_symbol]['id']
        target_name = currencies[target_symbol]['name']
        try:
            response = requests.get(f'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids={target_code}')
            response.raise_for_status()
            data = response.json()
            if data and data[0]['current_price'] is not None:
                exchange_rate = data[0]['current_price']
                mb.showinfo('Курс обмена',
                            f'Курс: {exchange_rate} USD за 1 {target_name}')
            else:
                mb.showerror('Ошибка',
                            f'Цена {target_name} недоступна')
        except Exception as er:
            mb.showerror('Ошибка', str(er))
    else:
        mb.showwarning('Внимание', 'Выберите криптовалюту из списка')


coins = load_cryptocurrencies()
currencies = {}

for coin in coins:
    currencies[coin['symbol'].upper()] = coin


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
