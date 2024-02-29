# Caesar Cipher Program

Welcome to the Caesar Cipher Program! This is a simple text-based program written in Python that 
allows you to encrypt and decrypt messages using the Caesar cipher.

## How to Use
1. Run the `Caesar_Cipher_Game.py` file using a Python interpreter.
2. Choose whether you want to encode (encrypt) or decode (decrypt) a message.
3. Enter the message you want to encrypt or decrypt.
4. Enter the shift number, which determines how many positions each letter should be shifted in the alphabet.
5. The program will display the encrypted or decrypted message.

## Features
- Simple text-based interface.
- Supports both encryption and decryption.
- Shifts letters in the alphabet by a specified number of positions.
- Allows wrapping around the alphabet (e.g., shifting 'z' by 1 results in 'a').

## Additional Information
- The Caesar cipher is a type of substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.
- This program uses a basic alphabet list for the cipher, which includes both lowercase and uppercase letters. Punctuation and numbers are not encrypted and remain unchanged in the output.
- The shift number can be any integer, but for simplicity, this program uses the modulus operator (%) to ensure that the shift wraps around the alphabet if it exceeds the length of the alphabet (26).

## Author
- [Supun Wickramarachchi](https://github.com/supunwickramarachchi)

Feel free to customize this program, add more features, or improve the interface. Have fun encrypting and decrypting messages with the Caesar cipher!
