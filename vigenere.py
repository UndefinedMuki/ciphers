from sys import version_info
from helpers import alphabet_position, rotate_character, read_ciphertext

py3 = version_info[0] > 2

def encrypt(mess, k):
    new_message = ""
    j = 0
    for i in range(len(mess)):
        if mess[i].isalpha():
            rot = alphabet_position(k[j % len(k)])
            j += 1
        else:
            rot = 0

        new_message += rotate_character(mess[i], rot)

    return new_message

def decrypt(mess, k):
    new_message = ""
    j = 0
    for i in range(len(mess)):
        if mess[i].isalpha():
            rot = 26 - alphabet_position(k[j % len(k)])
            j += 1
        else:
            rot = 0

        new_message += rotate_character(mess[i], rot)

    return new_message

def main():

    ciphertext = read_ciphertext()
 
    print("Ciphertext: " + ciphertext)
    print()

    if py3:
        key = input("Enter key: ")
    else:
        key = raw_input("Enter key: ")

    print(decrypt(ciphertext,key))

if __name__ == '__main__':
    main()
