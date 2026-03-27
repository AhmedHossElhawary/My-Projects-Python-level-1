import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
class User:
    def __init__(self, counter, first, last, email, password, status):
        self.id = counter
        self.full = f"{first} {last}"
        self.ml = email 
        self.pw = password
        self.stat = status

users_list = []
counter = 1

while True:
    print("\n--- Welcome to Gym Membership Management ---")
    chose = input("1. Add new Member\n2. Display all Members\n3. Search about a Member\n4. Exit\nEnter choice: ")
    if chose == "1":
        clear_screen()
        ask1 = input("Enter the first name: ")
        ask2 = input("Enter the last name: ")
        ask3 = input("Enter the Email: ")
        ask4 = input("Enter the password: ")
        ask5 = input("Status (active\inactive) : ") or "Inactive"
        ask5 = ask5[0].upper() + ask5[1:].lower()
        while ask5 not in ["Active" , "Inactive"]:
            ask5 = input("Please Enter active or inactive : ")
            ask5 = ask5[0].upper() + ask5[1:].lower()
        new_user = User(counter,ask1, ask2, ask3, ask4,ask5)
        users_list.append(new_user)
        counter += 1
        print("\nMember added successfully!")

    elif chose == "2":
        clear_screen()
        if not users_list:
            print("\nNo Member found.")
        else:
            print("\n--- Current Members ---")
            for u in users_list:
                print(f"ID : {u.id}\nName: {u.full}\nEmail: {u.ml}\nStatus: {u.stat}\n-----------------------------")

    elif chose == "3":
            clear_screen()
            q = input("Search (ID, Name, or Status): ").lower()
            for u in users_list:
                if q == u.id or q in u.full.lower() or q == u.stat.lower():
                    print(f"FOUND -> ID: {u.id}\nName: {u.full}\nEmail: {u.ml}\nStatus: {u.stat}\n-----------------------------")
                else:
                    print("Not Found")
            input("\nSearch finished. Enter to continue...")

    elif chose == "4":
        print("Goodbye!")
        break
    
    else:
        print("Invalid input. Please enter 1, 2, 3, or 4.")
    
        