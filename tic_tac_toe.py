'''
Github - https://github.com/bhuvan3sh
mail@id - abhuvanesh501@gmail.com


Tic-Tac-Toe Game in python. There are 2 players with marker 'X' and 'O'. The first one to create the combination of 3 in linear pattern wins the game. Re-run the program to play one again or add a menu with while loop to play till you are tired ;)

Feel Free to modify the code, no credits required

'''


map = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '] # Initial string values in the map
player = 1          # Value of player

# Result flags
Win = 1
Draw = -1
Running = 0
Stop = 1

Game = Running  # Value to determine whether the game is running or terminated



def Drawmap():      # Printing the results on the map based on player's decisions
    print(" %c | %c | %c " % (map[1], map[2], map[3]))
    print("___|___|___")
    print(" %c | %c | %c " % (map[4], map[5], map[6]))
    print("___|___|___")
    print(" %c | %c | %c " % (map[7], map[8], map[9]))
    print("   |   | \n")


def validMove(x):           # Function to check the validity and availability to make a move on the map (checking whether the space is empty or occupied).
    if map[x] == ' ':
        return True
    else:
        return False


def result():               # Function to check the possible combination to match pattern and declare a winner.
    global Game             # Declaring a global variable

    if map[1] == map[2] and map[2] == map[3] and map[1] != ' ':
        Game = Win
    elif map[4] == map[5] and map[5] == map[6] and map[4] != ' ':
        Game = Win
    elif map[7] == map[8] and map[8] == map[9] and map[7] != ' ':
        Game = Win
    elif map[1] == map[4] and map[4] == map[7] and map[1] != ' ':
        Game = Win
    elif map[2] == map[5] and map[5] == map[8] and map[2] != ' ':
        Game = Win
    elif map[3] == map[6] and map[6] == map[9] and map[3] != ' ':
        Game = Win
    elif map[1] == map[5] and map[5] == map[9] and map[5] != ' ':
        Game = Win
    elif map[3] == map[5] and map[5] == map[7] and map[5] != ' ':
        Game = Win
    elif map[1] != ' ' and map[2] != ' ' and map[3] != ' ' and \
            map[4] != ' ' and map[5] != ' ' and map[6] != ' ' and \
            map[7] != ' ' and map[8] != ' ' and map[9] != ' ':
        Game = Draw
    else:
        Game = Running


print("Tic-Tac-Toe")                                        # Begning of the Game
print("Player 1's marker: [X] \nPlayer 2's marker [O]\n\n")


while Game == Running:      # Loop running until the result is win (or) loose (or) tie.

    Drawmap()               # Function call to draw map for 1st players choice

    if player % 2 != 0:
        print("Player 1's chance")
        Mark = 'X'
    else:
        print("Player 2's chance")
        Mark = 'O'

    choice = int(input("Enter the position between [1-9] where you want the marker: "))
    if validMove(choice):
        map[choice] = Mark
        player += 1
        result()


    Drawmap()               # Function call to draw map for 2nd players choice

    if Game == Draw:        # Printing result
        print("Game Draw")
    elif Game == Win:
        player -= 1
        if player % 2 != 0:                                             
            print("Player 1 Won")
        else:
            print("Player 2 Won")
