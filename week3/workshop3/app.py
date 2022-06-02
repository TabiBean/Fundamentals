from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register


database = {"admin" : "password123"} #Dictionary used to store names and passwords
donations = [] #Donations list used to store the donations from users
authorized_user = "" #The person who is currently registered and logged in



while True:
    show_homepage()
    if authorized_user == "":   
        print("You must be logged in to donate.")
    elif authorized_user != "":
        print("Logged in as: ", authorized_user)

    choice = input("\nPlease choose an option: ")

    if choice == "1": #Login
        username = input("What is your username?")
        password = input("What is your password?")
        authorized_user = login(database, username, password)
 
    elif choice == "2": #Register
        username = input("What is your username?")
        password = input("What is your password?")
        authorized_user = register(database, username)
        if authorized_user != "":
            database[username] = password  
     
    elif choice == "3": #Accept the donation
        if authorized_user == "":
            print("You are not logged in.")
        else:
            donation_string = donate(authorized_user)
            donations.append(donation_string)
            print(donation_string)

    elif choice == "4":
        show_donations(donations)

    elif choice == "5":
        print("\nGoodbye")
        quit()
    else: 
        print("\nInvalid Choice. Try again.")



