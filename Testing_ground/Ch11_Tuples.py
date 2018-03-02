def sort_contacts(contacts):
    contact_list = []
    for name in contacts:
        contact_list.append(name)
        
    contact_list.sort()

    output = list(get_value(name, contacts[name]) for name in contact_list)
    return(output)

def get_value(strkey, tplvalue):
    bob = (strkey, tplvalue[0], tplvalue[1])
    return(bob)

def main():
    print(sort_contacts({"Horney, Karen": ("1-541-656-3010", "karen@psychoanalysis.com"),
    "Welles, Orson": ("1-312-720-8888", "orson@notlive.com"),
    "Freud, Anna": ("1-541-754-3010", "anna@psychoanalysis.com")}))

if __name__ == "__main__":
    main()