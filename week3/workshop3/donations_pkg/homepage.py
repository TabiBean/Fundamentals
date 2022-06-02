

#This is the menu screen that should continue to populate as users select items.
def show_homepage():
    print("\n     === DonateMe Homepage ===     ")
    print("-----------------------------------")
    print("| 1.   Login   | 2.   Register    |")
    print("-----------------------------------")
    print("| 3.   Donate  | 4.Show Donations |")
    print("-----------------------------------")
    print("|             5. Exit             |")
    print("-----------------------------------")

def donate(username): #Accepts the donation
    donation_amt = input("Enter amount to donate:")
    donation_string = username + " donated $" + donation_amt
    print("Thank you for your donation!")
    return donation_string

def show_donations(donations): #Tracks the donation
    print("\n      ---All Donations---      ")
    if len(donations) == 0:
        print("Currently, there are no donations.")
    else:
        for donors in donations:
            print(donors)



    