import requests
import json
from tkinter import Tk
from tkinter import Entry
from tkinter import Label
from tkinter import Button

root = Tk()
root.title('Ковылин Алексей')
root.geometry('400x400')

def Give_to_file():
    usname = Entry_user.get() 
    url = f'github.com/openshift/origin'

    user_data = requests.get(url).json()
    need_keys = ['company', 'created_at', 'email', 'id', 'name', 'url']

    data = dict()

    for i in need_keys:
        data[i] = user_data.get(i) 
        with open('C://Users/User/Desktop/vvod.txt', 'w') as file:
            file.write(json.dumps(data, indent = 4))

lbl = Label(text='Введите Имя Пользователя: ')
lbl.grid(column=0, row=0)
Entry_user = Entry(root)
Entry_user.grid(column=0, row=1)
Button_file = Button(root, text='Получить данные', command=Give_to_file)
Button_file.grid(column=1, row=1)



root.mainloop()