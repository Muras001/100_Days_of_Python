
# print(r'''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
# |                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************
# ''')


#Welcome Remarks
print("Welcome to Treasure Island Your Mission is to Find The Treasure:")

#Ask user for input on which way they would like to go
ways = input("Choose what way would like to go? left or right?\n ")

#Outcomes based on user input
if ways == "left":
    print("Game over!!")
elif ways == "right":
    river = input("Your in front of a river chose how to cross it? swim or wait?")
    if river == "swim":
        print("game over!! You were eaten by crocodiles")
    else:
        door = input("Your almost there, you given three doors, red, blue, yellow. chose one?")
        if door == "red":
            print("game over ! you got consumed by fire")
        elif door == "blue":
            print("game over!! You froze to death")
        else:
            print("congratulations You Won!!")
else:
    print("Incorrect Input!! Game over even before it started!!")




