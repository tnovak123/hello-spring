def get_char_count(joe):
    #count the different characters in joe
    c = dict()
    if joe != "":
        for char in joe:
            if char not in c:
                c[char] = joe.count(char)
            else:
                continue
    else:
        print("The string is empty.")

    return(c)

def main():
    print(get_char_count(input("Give me characters to count.")))

if __name__ == "__main__":
    main()