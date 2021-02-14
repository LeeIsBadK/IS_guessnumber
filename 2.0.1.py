# Base 2 Color Guesser
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
color_list=["Red","Green","Blue","Pink","Yellow","Orange","Puple"]

def round_cnt(times):
    if times == 0:
        display = ["Red",'Green','Yellow','Puple']
    elif times == 1:
        display = ['Blue','Green','Orange','Puple']
    else:
        display = ['Pink','Yellow','Orange','Puple']
    global P
    # Shuffle number
    P = sorted (display, key=lambda k: random.random ())
    return P


# define function to control programe

def time_cnt():
    if i == 3:
        # Hide Guess label
        number_label.pack_forget ()
        yes_button.pack_forget ()
        no_button.pack_forget ()

        # Show Result
        if User == 0:
            output_label.configure (text='Error, Please try again')
        else:
            Color=color_list[User-1]
            output_label.configure (text="Your color is %s" % Color)
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
                        text='\n Think color in mind and check that. Are there have your number in mind?.\n',
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
