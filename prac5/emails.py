
def main():
    """transform email to name."""
    email_to_name = {}
    email_address = input("pls enter your email: ")
    while email_address != "":
        name = get_name(email_address)
        confirmation = input("Is your name {}? (Y/n) ".format(name))
        if confirmation.upper() == "N" or confirmation == "NO":
            name = input("Name: ")
        elif confirmation.upper() == "Y" or confirmation.upper() == "YES" or confirmation.upper() == " ":
            pass
        else:
            print("not valid! plz enter again.")
            name = get_name(email_address)
        email_to_name[email_address] = name
        email_address = input("Email: ")
    for email_address, name in email_to_name.items():
        print("{} ({})".format(name, email_address))

def get_name(email):
    """get name from email address."""
    find_at = email.split('@')[0]
    find_dot = find_at.split('.')
    name = " ".join(find_dot).title()
    return name


if __name__ == '__main__':
    main()