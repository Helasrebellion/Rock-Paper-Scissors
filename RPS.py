from tkinter import *
import tkinter.font as font
import random

player_score = 0
computer_score = 0
options = [('rock',0), ('paper',1), ('scissors',2)]

def player_choice(player_input):
    global player_score, computer_score

    computer_input = get_computer_choice()

    player_choice_label.config(text = 'Your Selection : ' + player_input[0])
    computer_choice_label.config(text = 'Computer Selection : ' + computer_input[0])

    if(player_input == computer_input):
        winner_label.config(text = "It's a tie, try again.")
    elif((player_input[1] - computer_input[1]) % 3 == 1):
        player_score += 1
        winner_label.config(text="You Won! Nicely done!")
        player_score_label.config(text = 'Your Score : ' + str(player_score))
    else:
        computer_score += 1
        winner_label.config(text="The Computer won, try again.")
        computer_score_label.config(text='Your Score : ' + str(computer_score))

def get_computer_choice():
    return random.choice(options)

game_window = Tk()
game_window.title("Rock Paper Scissors")

app_font = font.Font(size = 12)

game_title = Label(text = 'Rock Paper Scissors', font = font.Font(size = 20), fg = 'grey')
game_title.pack()

winner_label = Label(text = "Select Your Hand", fg = 'Black', font = font.Font(size = 30), pady = 8)
winner_label.pack()

input_frame = Frame(game_window)
input_frame.pack()

player_options = Label(input_frame, text = "")
player_options.grid(row = 0, column = 0, pady = 8)

rock_btn = Button(input_frame, text = 'Rock', width = 25, bd = 0, bg = 'mediumpurple1', pady = 6, command = lambda: player_choice(options[0]))
rock_btn.grid(row = 1, column = 1, padx = 10, pady = 12)

paper_btn = Button(input_frame, text = 'Paper', width = 25, bd = 0, bg = 'palevioletred', pady = 6, command = lambda: player_choice(options[1]))
paper_btn.grid(row = 1, column = 2, padx = 10, pady = 12)

scissors_btn = Button(input_frame, text = 'Scissors', width = 25, bd = 0, bg = 'mediumspringgreen', pady = 6, command = lambda: player_choice(options[2]))
scissors_btn.grid(row = 1, column = 3, padx = 10, pady = 12)

score_label = Label(input_frame, text = 'Score : ', font = app_font, fg = 'grey')
score_label.grid(row = 2, column = 0)

player_choice_label = Label(input_frame, text = 'You Selected : ', font = app_font)
player_choice_label.grid(row = 3, column = 1, pady = 5)

player_score_label = Label(input_frame, text = 'Your Score : 0', font = app_font)
player_score_label.grid(row = 3, column = 2, pady = 5)

computer_choice_label = Label(input_frame, text = 'Computer Selected : ', font = app_font, fg = 'black')
computer_choice_label.grid(row = 4, column = 1, pady = 5)

computer_score_label = Label(input_frame, text = 'Computer Score : 0', font = app_font, fg = 'black')
computer_score_label.grid(row = 4, column = 2, padx = (10,0), pady = 5)

game_window.geometry('800x400')
game_window.mainloop()
