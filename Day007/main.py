import random


# Imports word_list from hangman_words, and stages, logo from hangman_art module.
from hangman_words import word_list
from hangman_art import stages,logo

lives = 6

# Prints logo form hangman.arts module
print(logo)

chosen_word = random.choice(word_list)


placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    # Shows user how many lives they have left.
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    # If user re-enters already guessed letter prints the letter and lets them know they already guessed it.
    if guess in correct_letters:
        print(f"You already guessed the letter{guess}")
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    # If letter is not in the chosen word print letter and let them know.

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed '{guess}' that is not in the word. You lose a life.")

        if lives == 0:
            game_over = True


            #Prints the correct answer.
            print(f"***********************It was {chosen_word} YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])
