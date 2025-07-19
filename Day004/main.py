import random
from random import choices

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game = [rock, paper, scissors]
game_option = ["rock", "paper", "scissors"]

my_choice = int(input("What is your choice, 0 = rock, 1 = paper, 2 = scissors:\n"))
print(f"Your chose: {game_option[my_choice]}")
print(game[my_choice])

comp_choice = random.randint(0,2)
print(f"Computer chose: {game_option[comp_choice]}")
print(game[comp_choice])


if my_choice == comp_choice:
    print("It is a tie!!")
elif my_choice == 0 and comp_choice == 2:
    print("You won!!")
elif my_choice == 1 and comp_choice == 0:
    print("You Won!!")
elif my_choice == 2 and comp_choice == 1:
    print("You Won!!")
else:
    print("You lost to a Robot!!")

