# Import and print the logo from art.py when the program starts.
from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    for letter in original_text:
        if letter in alphabet:
            if encode_or_decode == "decode":
                shifted_position = alphabet.index(letter) - shift_amount
                shifted_position %= len(alphabet)
                output_text += alphabet[shifted_position]
            elif encode_or_decode == "encode":
                shifted_position = alphabet.index(letter) + shift_amount
                shifted_position %= len(alphabet)
                output_text += alphabet[shifted_position]
        else:
             output_text += letter
    print(f"Here is the {encode_or_decode}d result: {output_text}")


# restarts the cipher program?
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart =input("Type 'yes' if you want to go again. Otherwise, type 'no':\n")
    if restart == 'no':
        should_continue = False
        print("Goodbye")
