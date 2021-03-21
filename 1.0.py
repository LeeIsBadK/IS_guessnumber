#Base 2 number 1-7
# Base 2 number 1-63 Guesser
# Author : Kittiphat Leesombatwathana, Kongsak Raksapakdee
# Instructor : Kannika Thada, Kanphakpim Udomwong, Sompit Phumchaung
# From Manchasuksa School: Manchakhiri, Khonkaen Thailand.
# This is independent study project (Grade 11)
# Version 1.0 (1/2/2021)

p = 0
for i in range(6):
    k = 0
    if i == 0:
        set = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51,
                   53,
                   55, 57, 59, 61, 63}
    elif i == 1:
        set = {2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31, 34, 35, 38, 39, 42, 43, 46, 47, 50, 51,
                   54,
                   55, 58, 59, 62, 63}
    elif i == 2:
        set = {4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31, 36, 37, 38, 39, 44, 45, 46, 47, 52, 53,
                   54,
                   55, 60, 61, 62, 63}
    elif i == 3:
        set = {8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31, 40, 41, 42, 43, 44, 45, 46, 47, 56, 57,
                   58,
                   59, 60, 61, 62, 63}
    elif i == 4:
        set = {16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 48, 49, 50, 51, 52, 53, 54, 55, 56,
                   57,
                   58, 59, 60, 61, 62, 63}
    else:
        set = {32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56,
                   57,
                   58, 59, 60, 61, 62, 63}
    while k == 0:
        print (set)
        Bul = input (str ("Do you have your number? (Y/N) \n>>>".upper ())).upper ()
        if Bul == 'Y':
            p += 2 ** (i)
            k = 1
        elif Bul == 'N':
            k = 1
        else :
            print("Wrong command, please try again \n")
    if i == 5:
        print ("Your number is %d" % p)
        input()
