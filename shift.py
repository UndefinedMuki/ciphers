from sys import version_info, argv, exit
from helpers import rotate_character, read_ciphertext

py3 = version_info[0] > 2

def bruteForce(ciphertext):
    for i in range(1, 26):
        plaintext = decrypt(ciphertext, i)

        print(plaintext)
        print()

        if py3:
            print("Shift: " + str(i))
            decrypted = input("Is plaintext decrypted? (y/n):  ")
        else:
            print("Shift: " + str(i))
            decrypted = raw_input("Is plaintext decrypted? (y/n):  ")

        if decrypted == 'y':
            exit()

def decrypt(text, rot):
    message = ""
    for char in text:
        message += rotate_character(char, rot)

    return message

def main():
    ciphertext = read_ciphertext()
 
    print("Ciphertext: " + ciphertext)
    print()

    if py3:
        bruteforce = input("Brute-force? (y/n): ")
    else:
        bruteforce = raw_input("Brute-force? (y/n): ")

    print()

    if bruteforce == 'y':
        bruteForce(ciphertext)

    elif bruteforce == 'n':
        if py3:
            key = int(input("Enter key: "))
        else:
            key = int(raw_input("Enter key: "))

        plaintext = decrypt(ciphertext, key)
        print(plaintext)
    else:
        print("Invalid character")

if __name__ == '__main__':
    main()