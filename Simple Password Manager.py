FILENAME = "passwords.txt"
def add_password():
    service = input("Enter service name:")
    username = input("Enter username:")
    password = input("Enter the password:")

    with open(FILENAME, "a") as f:
        f.write(f"{service} | {username} | {password}\n")
    print("Password is saved!\n")

def view_passwords():
    try:
        with open(FILENAME, "r") as f:
            data = f.read()
            if data.strip() == "":
                print("No passwords saved yet.\n")
            else:
                print("\n----Saved Passwords----")
                print(data)
    except FileNotFoundError:
        print("No Passwords saved yet.\n")

def main():
    while True:
        print("=======SIMPLE PASSWORDS MANAGER=======")
        print("1.Add a password")
        print("2.View Passwords")
        print("3.Exit")
        ch = input("Enter an option:")
        if ch == '1':
            add_password()
        elif ch == '2':
            view_passwords()
        elif ch == '3':
            print("Goodbye")
            break
        else:
            print("Invalid choice, Try again\n")

if __name__ == "__main__":
    main()