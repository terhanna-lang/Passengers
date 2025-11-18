import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox

attempts = 0
target = random.randint(1, 100)

def game():
    global attempts, target

    guess = int(main_tf.get())

    attempts += 1

    if target > guess:
        messagebox.showinfo(title="Попробуйте ещё раз!", message="Загаданное число больше!")
    elif target < guess:
        messagebox.showinfo(title="Попробуйте ещё раз!", message="Загаданное число меньше!")
    else:
        messagebox.showinfo(title="Вы выиграли!", message=f"Поздравляем! Вы угадали число {guess} с {attempts} попытки.")
        target = random.randint(1, 100)
        attempts = 0

def give_up():
    global target
    messagebox.showinfo(title="Вы сдались!", message=f"Вы сдались. Загаданным числом было {target}")
    target = random.randint(1, 100)

window = tk.Tk()
window.title("Угадайка")
window.geometry('600x500')

frame = Frame(
    window,
    padx = 10,
    pady = 10
)
frame.pack(expand=True)

main_lb = Label(
    frame,
    text="Угадайте число от 1 до 100"
)
main_lb.grid(row=3, column=1)

main_tf = Entry(
    frame
)
main_tf.grid(row=3, column=2)

main_btn = Button(
    frame,
    text="Ввод",
    command=game
)
main_btn.grid(row=4, column=2)

giveup_btn = Button(
    frame,
    text="Сдаться",
    command=give_up
)
giveup_btn.grid(row=5, column=2)

window.mainloop()