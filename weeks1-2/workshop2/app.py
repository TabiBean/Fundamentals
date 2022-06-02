from banking_pkg.account import *

def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

balance = 0

while True:
    print("    ===Automated Teller Machine===     ")
    name = input("Enter name to register:")
    name_length = len(name)
    if name_length < 1:
        print("You must enter a name.")
    elif name_length > 10:
        print("The maximum name length is 10 characters.")
    else:
        break
   
while True:
    pin = input("Enter PIN:")
    pin_length = len(pin)
    try:
        int(pin)
        it_is = True
    except ValueError:
        it_is = False
    if it_is == False or pin_length != 4:
        print("PIN must contain 4 numbers.")
    elif pin_length == 4:
        break

print(name + " has been registered with a starting balance of $" + str(balance))

while True:
    print("LOGIN")
    name_to_validate = input("Enter name: ")
    pin_to_validate = input("Enter PIN: ")

    if name_to_validate == name and pin_to_validate == pin:
        print("Login successful!")
        break
    else:
        print("Invalid credentials!")

while True:
    atm_menu(name)
    option = input("Choose an option: ")

    if option == "1":
        show_balance(balance)
    elif option == "2":
        balance = deposit(balance)
        show_balance(balance)
    elif option == "3":
        balance = withdraw(balance)
        show_balance(balance)
    elif option == "4":
        logout(name)
        break
    else:
        print("Invalid Entry!")
        logout(name)
        break
   
    
    
    

    

