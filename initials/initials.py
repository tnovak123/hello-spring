def get_initials(fullname):
#"""Given a person's name, returns the person's initials (uppercase) """
# todo your code here
    i = ""
    names = []
    name = ""
    if fullname != "":
        names = fullname.split(" ")
        for name in names:
            if name != "":
                i = i + name[0]
            else:
                continue
    else:
        print("No name was given.")

    i = i.upper()
    return(i)

def main():
    print(get_initials(input("What is your full name?")))

if __name__ == "__main__":
    main()