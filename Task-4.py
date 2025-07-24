#Task - 4   Rock-Paper-Scissors Game
import tkinter as tk
from tkinter import messagebox
import random


choices = ['Rock', 'Paper', 'Scissors']

def play(userchoice):
    global userscore, computerscore

    computerchoice = random.choice(choices)
    result = " "

    if userchoice == computerchoice:
        result = "It's a Tie!"
    elif (userchoice == 'Rock' and computerchoice == 'Scissors') or \
         (userchoice == 'Paper' and computerchoice == 'Rock') or \
         (userchoice == 'Scissors' and computerchoice == 'Paper'):
        result = "You Win!"
        userscore += 1
    else:
        result = "Computer Wins!"
        computerscore += 1

    update_result(userchoice, computerchoice, result)

def update_result(user, computer, result):
    user_choice_label.config(text=f"You choosed: {user}")
    comp_choice_label.config(text=f"Computer choosed: {computer}")
    result_label.config(text=result)
    score_label.config(text=f"Score - You: {userscore} | Computer: {computerscore}")

def reset_game():
    global userscore, computerscore
    userscore = 0
    computerscore = 0
    user_choice_label.config(text="")
    comp_choice_label.config(text="")
    result_label.config(text="")
    score_label.config(text="Score - You: 0 | Computer: 0")


userscore = 0
computerscore = 0


window = tk.Tk()
window.title("ROCK-PAPER-SCISSORS Game")
window.geometry("600x600")
window.resizable(True, False)

title = tk.Label(window, text="Rock - Paper - Scissors", font=("Times New Roman", 30, "bold"))
title.pack(pady=10)


button_frame = tk.Frame(window)
button_frame.pack(pady=10)

rock_butn = tk.Button(button_frame, text="Rock", width=20, command=lambda: play('Rock'))
paper_butn = tk.Button(button_frame, text="Paper", width=20, command=lambda: play('Paper'))
scissors_butn = tk.Button(button_frame, text="Scissors", width=20, command=lambda: play('Scissors'))

rock_butn.grid(row=0, column=0, padx=5)
paper_butn.grid(row=0, column=1, padx=5)
scissors_butn.grid(row=0, column=2, padx=5)


user_choice_label = tk.Label(window, text="", font=("Arial", 12))
user_choice_label.pack()

comp_choice_label = tk.Label(window, text="", font=("Arial", 12))
comp_choice_label.pack()

result_label = tk.Label(window, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=10)

score_label = tk.Label(window, text="Score - You: 0 | Computer: 0", font=("Arial", 12))
score_label.pack(pady=5)


reset_butn = tk.Button(window, text="Reset Game", command=reset_game, bg="red", fg="white")
reset_butn.pack(pady=10)


window.mainloop()
