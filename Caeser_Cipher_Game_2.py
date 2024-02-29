alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(start_text, shifted_ammount, cipher_direction):
    cipher_text = ""
    if cipher_direction == "decode":
        shifted_ammount *= -1
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shifted_ammount
            cipher_text += alphabet[new_position]
        else:
            cipher_text += letter
        
    print(f"The {cipher_direction}d text: {cipher_text}")
            


from Caeser_game_arts import logo
print(logo)

continue_game = True
while continue_game:
    direction = input("If you want to encrypt type 'encode' or decrypt type 'decode' : ")
    text = input("Enter yout message: ").lower()
    shift = int(input("Enter shift ammount: "))
    
    shift = shift % 26
    
    
    caeser(start_text = text, shifted_ammount = shift, cipher_direction = direction)

    game_future = input("Do you want to continue game (yes / no): ")
    if game_future == "no":
        continue_game = False
        print("* Thank you !! Play another time *")



