from caesar_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)

# def encrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_index = (alphabet.index(letter) + shift_amount) % len(alphabet)
#         cipher_text += alphabet[shifted_index]
#     print(f"Here is the encoded result: {cipher_text}")

# def decrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_index = (alphabet.index(letter) - shift_amount) % len(alphabet)
#         cipher_text += alphabet[shifted_index]
#     print(f"Here is the decoded result: {cipher_text}")

# testing encrypt and decrypt
# encrypt(original_text=text, shift_amount=shift)
# decrypt(original_text=text, shift_amount=shift)

# combining encrypt and decrypt functions
def caesar(original_text, shift_amount, encode_or_decode):
    cipher_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter not in alphabet:
            cipher_text += letter
        else:
            shifted_index = (alphabet.index(letter) + shift_amount) % len(alphabet)
            cipher_text += alphabet[shifted_index]

    print(f"Here is the {encode_or_decode}d result: {cipher_text}")

go_again = True

while go_again == True:
    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if direction not in ["decode", "encode"]:
            print("Invalid input. Please enter either encode or decode.")
        else:
            break

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    while True:
        restart = input("Type 'yes' if you want to go again. Otherwise, type 'no':\n").lower()
        if restart not in ["yes", "no"]:
            print("Invalid input. Please enter either yes or no.")
        else:
            break

    if restart == "no":
        go_again = False
        print("Goodbye")
