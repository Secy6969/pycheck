"""
Author - A Bhuvanesh
Github - https://github.com/Bhuvan3sh
Program - Snake, Water, Gun game between the user and computer
"""


import random                       #Importing random library

def game_win(comp,you):             #Defining the function to check the chance between computer and the user
    if comp == you:
        return None                 #tie
    elif comp == 's':
        if you == 'w':
            return False            #user's win
        else:
            return True             #computer's win
    elif comp == 'w':
        if you == 'g':
            return False            #user's win
        else:
            return True             #computer's win
    else:
        if you == 's':
            return False            #user's win
        else:
            return True             #computer's win


print("Welcome to snake, water and gun game!!!".center(80,"*"))            # starting of the program

print("Computer's turn: For Snake(s), Water(w), Gun(g)".center(80,"~"))

game_init = "Your turn: For Snake(s), Water(w), Gun(g). Choose wisely:-)"

flag= 0

for i in range(3):
    rand_no = random.randint(1,3)                               #using random library for computer's choice
    if rand_no == 1:
        comp = 's'
    elif rand_no == 2:
        comp = 'w'
    else:
        comp = 'g'



    print(game_init.center(80, "~"))
    char_size = 'swg'
    you = input("=")                            #User's input
    if you in char_size and len(you) == 1:      #condition to take only one input and only from selected characters
        a = game_win(comp,you)                  #calling the function
        print(f"computer chose {comp}")         #printing computer choice
        print(f"You chose {you}")               #printing users choice

        if a is None:                           #printing the evaluated result
            print("The match is tie")
            flag += 0

        elif not a:
            print("You lost")
            flag -=1

        else:
            print("You won")
            flag += 1
    else:
        print("Re-run the program and enter only one ch")       #condition if the input was not chosen properly

if you in char_size and len(you) == 1:
    a = "Your total score is"
    g = a.center(50,"*")

    print(g)
    ab = str(flag)                                #print the score
    print("\n"+ab.center(50,"_"))
    win_me = "You have won the league with computer"

    if flag==3:
        print(win_me.center(50,"^"))