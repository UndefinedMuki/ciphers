alphabet = "abcdefghijklmnopqrstuvwxyz"

def alphabet_position(letter):
    
    letter = letter.lower()
    pos = alphabet.find(letter)
    return pos

def rotate_character(char, rot):
    
    if char.isalpha():
        pos = (alphabet_position(char.lower()) + rot) % 26

        if char.isupper():
            new_char = alphabet[pos].upper()
        else:
            new_char = alphabet[pos]
    else:
        new_char = char

    return new_char

def read_ciphertext():
    cipherfile = open("./cipher.txt", "r")
    ciphertext = cipherfile.read()
    cipherfile.close()

    return ciphertext