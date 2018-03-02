from helpers import alphabet_position, rotate_character

def encrypt(text, key):
    newtext = ""
    rota = 0
    rotb = 0
    for char in text:
        if char.isalpha() == True:
            rota = alphabet_position(key[rotb])
            newtext += rotate_character(char, rota)
            if rotb < (len(key) - 1):
                rotb += 1
            else:
                rotb = 0
        else:
            newtext += char
    
    return(newtext)

def main():
    inputtext2 = input("What do you want to encrypt?")
    inputkey = input("What keyword do you want to use?")
    if inputkey.isalpha() == True:
        print(encrypt(inputtext2, inputkey))
    else:
        pass
    
if __name__ == "__main__":
    main()