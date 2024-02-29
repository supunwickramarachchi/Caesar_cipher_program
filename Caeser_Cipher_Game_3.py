symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', 
           '[', ']', '{', '}', '|', '\\', ';', ':', "'", '"', '.', ',', '!', '@', 
           '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', 
           '{', '}', '|', '\\', ';', ':', "'", '"', '.', ',']

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(start_text, shift_ammount, cipher_direction):
    cipher_text = ""
    if direction == "encode":
        for letter in start_text:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = position + shift_ammount
                cipher_text += symbols[new_position]
            else:
                cipher_text += letter
        
            
    elif direction == "decode":
        shift_ammount *= -1
        for char in start_text:
            if char in symbols:
                position = symbols.index(char)
                new_position = position + shift_ammount
                cipher_text += alphabet[new_position]
            else:
                cipher_text += char
            
        
    print(f"The {cipher_direction}d text: {cipher_text}")
    
    

from Caeser_game_arts import logo
print(logo)

continue_game = True
while continue_game:

    direction = input("If you want to encrypt type 'encode' or decrypt type 'decode' : ")
    text = input("Enter your message: ").lower()
    shift = int(input("Enter shift amount: "))
    
    shift = shift % 26
    
    caeser(start_text = text, shift_ammount = shift, cipher_direction = direction)
    
    user = input("Do you want to continue the game (yes/ no): ")
    if user == "no":
        continue_game = False
        print("**** !!! Thak you !!! ****")
