import random
import time


# call for this when you want to create a new knight
def create_knights(knights):
    # creates a new list for the knight
    knights_data = []

    print("Lets create a knight!")

    # set the information up for the knight
    knights_data.append(str(input("What is the knights name: ")))

    # adds the information to the knight
    knights.append(knights_data)


# Battle function using random module and ascii art.
def battle(knights):
    random_number = random.randint(1, 2)
    if random_number == 1:
        print("""You have been defeated by the dragon
            ( _)                ( _)
           / / \\              / /\_\_
          / /   \\            / / | \ \
         / /     \\          / /  |\ \ \
        /  /   ,  \ ,       / /   /|  \ \
       /  /    |\_ /|      / /   / \   \_\
      /  /  |\/ _ '_| \   / /   /   \    \\
     |  /   |/  0 \0\    / |    |    \    \\
     |    |\|      \_\_ /  /    |     \    \\
     |  | |/    \.\ o\o)  /      \     |    \\
     \    |     /\\`v-v  /        |    |     \\
      | \/    /_| \\_|  /         |    | \    \\
      | |    /__/_ `-` /   _____  |    |  \    \\
      \|    [__]  \_/  |_________  \   |   \    ()
       /    [___] (    \         \  |\ |   |   //
      |    [___]                  |\| \|   /  |/
     /|    [____]                  \  |/\ / / ||
snd (  \   [____ /     ) _\      \  \    \| | ||
     \  \  [_____|    / /     __/    \   / / //
     |   \ [_____/   / /        \    |   \/ //
     |   /  '----|   /=\____   _/    |   / //
  __ /  /        |  /   ___/  _/\    \  | ||
 (/-(/-\)       /   \  (/\/\)/  |    /  | /
               (/\/\)           /   /   //
                      _________/   /    /
                     \____________/    
        
        """)
    else:
        print("""victorious!!!
                   .--.
            /.--.\
            |====|
            |`::`|
        .-;`\..../`;_.-^-._
 /\\   /  |...::..|`   :   `|
 |:'\ |   /'''::''|   .:.   |
@|\ /\;-,/\   ::  |..:::::..|
`||\ <` >  >._::_.| ':::::' |
 || `""`  /   ^^  |   ':'   |
 ||       |       \    :    /
 ||       |        \   :   /
 ||       |___/\___|`-.:.-`
 ||        \_ || _/    `
 ||        <_ >< _>
 ||        |  ||  |
 ||        |  ||  |
 ||       _\.:||:./_
 \/ jgs  /____/\____\
        
        
        
        
        """

              )


# Function to select weapons
def weapon(knights):
    x = []
    weapons = ["""Mace 
          |\
          | \        /|
          |  \____  / |
         /|__/AMMA\/  |
       /AMMMMMMMMMMM\_|
   ___/AMMMMMMMMMMMMMMA
   \   |MVKMMM/ .\MMMMM\
    \__/MMMMMM\  /MMMMMM---
    |MMMMMMMMMMMMMMMMMM|  /
    |MMMM/. \MM.--MMMMMM\/
    /\MMM\  /MM\  |MMMMMM   ___
   /  |MMMMMMMMM\ |MMMMMM--/   \-.
  /___/MMMMMMMMMM\|MM--M/___/_|   \
       \VMM/\MMMMMMM\  |      /\ \/
        \V/  \MMMMMMM\ |     /_  /
          |  /MMMV'   \|    |/ _/
          | /              _/  /
          |/              /| \'
                         /_  /
                         /  /   VK
    
    
    
    
    """, """Lance
                  /`-..___              
  ___________/        ````-----......_______
 (___________|                       _______::::::::=========----------
  _____      \     ___,,,,-----''''''
 /____/|      \,-''

    
    """, """Sword 
             .
        / \
       /   \
      /  |  \
      |  |  |
      |  |  |
      |  |  |
      |  |  |
      |  |  |
      |  |  |
      |  |  |
      |  |  |
      |  |  |
      |  |  |
      |  |  |
      |  |  |
      |  |  |
      |  |  |
      |  |  |
      |  |  |
 ____/|  |  |\____
/____/\___/\____/ )
(_______________)/
      |/////|
      |/////|
      |/////|
      |/////|
      |/////|
      |/////|
      |/////|

    
    
    
    """]
    x = (random.choice(weapons))
    print(x)


# Function to select team.

def team_colour():
    print("Please choose your team")
    print("1: house of lancelot")
    print("2: black kingdom")

    try:

        select = int(input("Select your option:  "))

        if select == 1:
            print("welcome to the house of lancelot")
        else:
            print("welcome to the black kingdom")

    except:
        print("try again")


# Function to choose companion
def companion():
    print("press 1 to choose Gwenivere")
    print("press 2 for Sir John")

    try:
        select = int(input("Select companion:  "))

        if select == 1:
            print("Gwen: will be a worthy leige")
        else:
            print("Sir John: At your service")
    except:
        print("Try again")


# Call a knight and change their data
def change_data(knights):
    print("---What would you like to update?---")
    print("1: knights name: " + knights[0])

    try:

        selection = int(input("Selection your option: "))

        if selection == 1:
            if knights_number == 0:
                print("You have a knight")
            knights[0] = str(input("what is their new name: "))
            print("Your knight's new name is: " + knights[0])
            return
        else:
            print("--- Please select a valid option ---")

    except:
        print("--- Try Again! ---")
        change_data(knights)


# Show the current knights and select one
def select_knight(knights):
    # Reset the list to print all the knights you have
    knights_number = 0
    print("What knight would you like to update?\n")
    while knights_number < int(len(knights)):
        print(str(knights_number + 1) + "knight's name:" + str(knights[knights_number][0]))
        knights_number += 1

    selection = (int(input("\nSelect the knights number: ")) - 1)
    change_data(knights[selection])


# This is the menu and we make our selections here
def menu(knights_number):
    # print the display options
    print("What do you want to do?")
    print("1: Create a new knight")
    print("2: Update your knight")
    print("3: Select weapon")
    print("4: Battle")
    print("5:Choose your kingdom")
    print("6: Choose companion")
    print("0: Exit")

    # Allow a selection to be tested
    try:

        # Takes the users selection option
        select = int(input("Selection number: "))
        print()  # Create a blank line

        # Create a new knight
        if select == 1:
            create_knights(knights)

            # Print out the knight that was made
            print("\n--- Your Knight ---\n")
            print("knight's name: " + str(knights[knights_number][0] + "\n"))
            knights_number += 1
            menu(knights_number)

        elif select == 2:
            if int(len(knights)) == 0:
                print("You need to create a knight first!! \n")
            else:
                select_knight(knights)
            menu(knights_number)
#Weapon selection with sleep timer for beautification purposes
        elif select == 3:
            weapon(knights)
            time.sleep(5)
            menu(knights_number)
#Link to battle function.
        elif select == 4:
            battle(knights)
            time.sleep(3)
            menu(knights_number)
#link to team selection
        elif select == 5:
            team_colour()
            time.sleep(5)
            menu(knights_number)
#link to choose a companion
        elif select == 6:
            companion()
            time.sleep(5)
            menu(knights_number)

#exit menu
        elif select == 0:
            print("--- All your knights! ---\n")

            # Reset the knights_number, to count all the knights
            knights_number = 0

            while knights_number < int(len(knights)):
                print(str(knights_number + 1) + "knight's name:" + str(knights[knights_number][0]))
                knights_number += 1

            if int(len(knights)) == 0:
                print("Wait... You have no knights! Have a number" + str(random.randint(0, 100)))

                # Required for catching integer
        else:
            print("--- Try Again! ---\n")
            menu(knights_number)

    # We are looking for integer selection
    except:
        print("--- Try Again! ---\n")
        menu(knights_number)


# Setting the scene
knights_number = 0
knights = []

# Run the program
menu(knights_number)
