#Caesar Cipher
#The Caesar cipher moves each letter forward in the alphabet by
#the key.  The resulting message has all the letters advanced by 'key'
#letters.
#To run the code, run the main() function

def caesar_cipher(message, key):
    result = ""

    for letter in message:
        if letter.isalpha():
            # Determine ASCII offset for uppercase or lowercase letters
            offset = ord('A') if letter.isupper() else ord('a')
            # Find the alphabetical index (0-25)
            pos = ord(letter) - offset
            # Shift position by key with wrap-around
            new_pos = (pos + key) % 26
            # Convert back to a character
            new_letter = chr(new_pos + offset)
            result += new_letter
        else:
            # Non-alphabetic characters remain unchanged
            result += letter

    return result

def main():
    message = input("Enter the message to encrypt: ")
    key = int(input("Enter the shift key (e.g., 3): "))
    encrypted = caesar_cipher(message, key)
    print("Encrypted message:", encrypted)

if __name__ == "__main__":
    main()
