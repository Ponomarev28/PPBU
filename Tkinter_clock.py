from tkinter import *
import time

window = Tk()
month = time.strftime('%B')
year = time.strftime('%Y')
day = time.strftime('%d')
match month:
    case 'September':
        month = 'Сентября'


m = Label(text=f'{day} {month}  {year}', font="Verdana 24 bold")
m.pack()
m.pack()

window.mainloop()