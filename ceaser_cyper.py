alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
            ]


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    # This is for when a user enters a shift that is greater than the number of
    # letters in the alphabet.
    shift = shift % 26


    # Shorter piece of code by making the code dynamic.

    def caesar(start_text, shift_amount, cipher_direction):
        end_text = ''
        if cipher_direction == "decode":
            shift_amount *= -1
        for char in start_text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position + shift_amount
                end_text += alphabet[new_position]
            else:
                end_text += char
        print(f"Here's the {direction}d result: {end_text}")


    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == "no":
        should_continue = False
        print("Goodbye!")



# def encrypt(plain_text, shift_amount):
#     cipher_text = ''
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}")
#
# def decrypt(decrypt_text, decrypt_shift_amount):
#     decipher_text = ''
#     for letter in decrypt_text:
#         decrypt_position = alphabet.index(letter)
#         new_decrypt_position = decrypt_position - decrypt_shift_amount
#         new_decrypt_letter = alphabet[new_decrypt_position]
#         decipher_text += new_decrypt_letter
#     print(f"The encoded text is {decipher_text}")
#
# if direction == 'encrypt':
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == 'decrypt':
#     decrypt(decrypt_text=text, decrypt_shift_amount=shift)
