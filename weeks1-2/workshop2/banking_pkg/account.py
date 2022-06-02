
def show_balance(balance):
    print("Current Balance: $", balance) 

def deposit(balance):
    amount = input("Enter amount to deposit: $")
    balance = balance + float(amount)
    return balance

def withdraw(balance):
    amount = input("Enter amount to withdraw: $")
    if float(amount) > balance:
        print("Where are you going to get that kind of money?")
        return balance
    else:
        balance = balance - float(amount)
        return balance
       
def logout(name):
    print("Goodbye " + name)



