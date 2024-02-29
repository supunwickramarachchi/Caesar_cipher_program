alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caeser(start_text, shif_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shif_amount *= -1
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shif_amount
            end_text += alphabet[new_position]
        else:
            end_text += letter
    print(f"Your {cipher_direction}d text: {end_text}")


from Caeser_game_arts import logo

print(logo)

continue_game = True
while continue_game:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    caeser(start_text=text, shif_amount=shift, cipher_direction=direction)

    user = input("Do you want to continue the game (yes / no): ")
    if user == "no":
        continue_game = False
        print("Thank you!!!")
