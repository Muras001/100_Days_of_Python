import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Level
easy_Password = ""
for letter in range(0,nr_letters):
    easy_Password += random.choice(letters)
for number in range(0,nr_numbers):
    easy_Password += random.choice(numbers)
for symbol in range(0, nr_symbols):
    easy_Password += random.choice(symbols)
print(easy_Password)

#Hard Level

hard_Password = []
for letter in range(0,nr_letters):
    hard_Password.append(random.choice(letters))
for number in range(0,nr_numbers):
    hard_Password.append(random.choice(numbers))
for symbol in range(0, nr_symbols):
    hard_Password.append(random.choice(symbols))

print(hard_Password)

hard_Password_final = " "
random.shuffle(hard_Password)
print(hard_Password)


for hard in hard_Password:
    hard_Password_final += hard
print(hard_Password_final)
