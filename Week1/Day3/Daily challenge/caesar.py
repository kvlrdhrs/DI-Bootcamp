def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                encrypted_text += chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def caesar_cipher():
    while True:
        choice = input("Do you want to encrypt or decrypt a message? (e/d): ").lower()
        if choice in ['e', 'd']:
            text = input("Enter the message: ")
            shift = int(input("Enter the shift value: "))
            if choice == 'e':
                print("Encrypted message:", encrypt(text, shift))
            else:
                print("Decrypted message:", decrypt(text, shift))
        else:
            print("Invalid choice. Please enter 'e' to encrypt or 'd' to decrypt.")

        cont = input("Do you want to perform another operation? (yes/no): ").lower()
        if cont != 'yes':
            break

if __name__ == "__main__":
    caesar_cipher()