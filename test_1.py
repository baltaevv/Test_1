# задание 3
from tkinter import *
from datetime import datetime

root = Tk()
root.title("Приветствия")
root.geometry("400x300")

greetings = [
    ("Доброе утро ", 9),
    ("Хорошего дня ", 11),
    ("Добрый вечер ", 18),
    ("Спокойной ночи ", 22)
]

listbox = Listbox(root, width=40, height=10, font=("Arial", 12))
listbox.pack(pady=20)

def show_greetings(filtered):
    listbox.delete(0, END)

    for text in filtered:
        listbox.insert(END, text)

def show_morning():
    morning = []

    for text, hour in greetings:
        if hour < 12:
            morning.append(text)

    show_greetings(morning)

def show_evening():
    evening = []

    for text, hour in greetings:
        if hour >= 12:
            evening.append(text)

    show_greetings(evening)

btn_morning = Button(
    root,
    text="Показать утренние приветствия",
    command=show_morning
)
btn_morning.pack(pady=5)

btn_evening = Button(
    root,
    text="Показать вечерние приветствия",
    command=show_evening
)
btn_evening.pack(pady=5)

now = datetime.now()
print(now.strftime("%H:%M:%S"))

root.mainloop()

# проверяет время и если <12 то выводит утренние приветствия, 
# если >=12 то вечерние если иначе то пусто

        
# задание 4
from tkinter import *
from datetime import datetime

root = Tk()
root.title("История приветствий")
root.geometry("400x350")

history = []

listbox = Listbox(root, width=45, height=12, font=("Arial", 12))
listbox.pack(pady=20)


def update_list():
    listbox.delete(0, END)
    for item in history:
        listbox.insert(END, item)


def add_greeting():
    time = datetime.now().strftime("%H:%M:%S")
    message = f"{time} — Приветствие"

    history.append(message)

    # оставляем только последние 5
    if len(history) > 5:
        history.pop(0)

    update_list()


Button(root, text="Добавить приветствие", command=add_greeting).pack()

root.mainloop()

# саздал окно и еще список для хранения данных, список на экран выводится через listbox,
#обновление списка, ограничение до 5 элементо, обнавление экрана, кнопка для добавления приветствия, 

        
        
