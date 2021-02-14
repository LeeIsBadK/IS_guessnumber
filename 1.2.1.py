# Base 2 number 1-63 Guesser
# Author : Kittiphat Leesombatwathana, Kongsak Raksapakdee
# Instructor : Kannika Thada, Kanphakpim Udomwong, Sompit Phumchaung
# From Manchasuksa School: Manchakhiri, Khonkaen Thailand.
# This is independent study project (Grade 11)
# Version 1.2.0 (7/2/2021)

import random
import tkinter as tk
from tkinter import Label

P = []
User = 0
i = 0


def round_cnt(times):
    if times == 0:
        display = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51,
                   53,
                   55, 57, 59, 61, 63]
    elif times == 1:
        display = [2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31, 34, 35, 38, 39, 42, 43, 46, 47, 50, 51,
                   54,
                   55, 58, 59, 62, 63]
    elif times == 2:
        display = [4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31, 36, 37, 38, 39, 44, 45, 46, 47, 52, 53,
                   54,
                   55, 60, 61, 62, 63]
    elif times == 3:
        display = [8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31, 40, 41, 42, 43, 44, 45, 46, 47, 56, 57,
                   58,
                   59, 60, 61, 62, 63]
    elif times == 4:
        display = [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 48, 49, 50, 51, 52, 53, 54, 55, 56,
                   57,
                   58, 59, 60, 61, 62, 63]
    else:
        display = [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56,
                   57,
                   58, 59, 60, 61, 62, 63]
    global P
    # Shuffle number
    P = sorted (display, key=lambda k: random.random ())
    return P


# define function to control programe

def time_cnt():
    if i == 6:
        # Hide Guess label
        number_label.pack_forget ()
        yes_button.pack_forget ()
        no_button.pack_forget ()

        # Show Result
        if User == 0:
            output_label.configure (text='Error, Please try again')
        else:
            output_label.configure (text="Your number is %d" % User)
        output_label.pack ()
        reset_label.pack ()


def Yes(event=None):  # When User Click Yes
    global User, i, number_label
    User += 2 ** i
    i += 1

    number_label.configure (text=round_cnt (i))
    time_cnt ()


def No(event=None):
    global i, number_label
    i += 1
    number_label.configure (text=round_cnt (i))
    time_cnt ()


def Reset(event=None):
    global i, User
    i = 0
    User = 0
    output_label.forget ()
    reset_label.forget ()
    number_label.configure (text=round_cnt (i))
    number_label.pack ()
    yes_button.pack ()
    no_button.pack ()


# GUI Section by Tkinker

window = tk.Tk ()

window.title ("Guess Number")
window.geometry ("1920x1080")

title_label = tk.Label (master=window,
                        text='\n Think numbers 1-63 in mind and check that. Are there have your number in mind?.\n',
                        font=("Arial", 28))
title_label.pack ()

number_label = Label (master=window, text=round_cnt (i), font=("Arial", 30), wraplength=600, justify="left", padx=20,
                      pady=40, height=5)
number_label.pack ()

yes_button = tk.Button (master=window, text='Yes', font=("Arial", 20), width=5, command=Yes)
no_button = tk.Button (master=window, text='No', font=("Arial", 20), width=5, command=No)
yes_button.pack (), no_button.pack ()

output_label = tk.Label (master=window, font=("Arial", 44))
output_label.pack ()

reset_label = tk.Button (master=window, text="Restart", font=("Arial", 44), command=Reset)

window.bind ('<Return>', yes_button)
window.bind ('<Return>', no_button)
window.mainloop ()
