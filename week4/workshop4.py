class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, new_name):
        self.new_name = new_name
    
    def change_pin(self, new_pin):
        self.new_pin = new_pin

    def change_password(self, new_password):
        self.new_password = new_password

class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

    def show_balance(self):
        return self.balance

    def withdrawl(self, withdrawl_amount):
        self.balance -= withdrawl_amount
        return self.balance

    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        return self.balance
    
    def transfer(self, user2, amount_to_transfer):
        print("You are transferring $", amount_to_transfer, "to",user2.name)
        print("Authentication required.")
        pin_check = input("Enter your pin?")
        if pin_check == self.pin:
            print("Transfer authorized.")
            print("Transferring $", amount_to_transfer, "to", user2.name)
            self.balance -= amount_to_transfer
            user2.balance += amount_to_transfer

            return True
        else:
            print("Invalid PIN. Transaction cancelled.")
            return False
        
    def request_money(self, user2, amount_to_transfer):
            print("You are requesting $", amount_to_transfer, "from", user2)
            print("User authentication is required...")
            pin_check = input("What is the pin number for the account you wish to receive money from?")
            password_check = input("What is your password?")
            if self.password == password_check and pin_check == user2.pin:
                self.balance += amount_to_transfer
                user2.balance -= amount_to_transfer
                return True
            else:
                print("Invalid PIN or Password. Transaction cancelled.")
                return False

# --------DRIVER CODE FOR TASK 1--------
# user1 = User("Bob", 1234, "password")
# print(user1.name, user1.pin, user1.password)

# --------DRIVER CODE FOR TASK 2--------
# user2 = User("Bob", 1234, "password")
# print(user2.name, user2.pin, user2.password)
# user2.change_name("Bobby")
# user2.change_pin(4321)
# user2.change_password("newpassword")
# print(user2.new_name, user2.new_pin, user2.new_password)

# # # --------DRIVER CODE FOR TASK 3--------
# user_tom = BankUser("Tom", 4567, "jerry")
# print(user_tom.name, user_tom.pin, user_tom.password, user_tom.balance)

# # --------DRIVER CODE FOR TASK 4--------
# user4 = BankUser("Tiffany", 1111, "password4")
# print(user4.name, "has an account balance of:", user4.show_balance())
# user4.deposit(500)
# print(user4.name, "has an account balance of", user4.show_balance())
# user4.withdrawl(100)
# print(user4.name, "has an account balance of:", user4.show_balance())

# # --------DRIVER CODE FOR TASK 5--------
user_tom = BankUser("Tom", "1111", "jerry")
user4 = BankUser("Tiffany", "1234", "password4")

user4.deposit(5000)

print(user4.name, "has an account balance of", user4.show_balance())
print(user_tom.name, "has an account balance of", user_tom.show_balance())

user4.transfer(user_tom, 500)

print(user4.name, "has an account balance of", user4.show_balance())
print(user_tom.name, "has an account balance of", user_tom.show_balance())

user4.request_money(user_tom, 250)

print(user4.name, "has an account balance of", user4.show_balance())
print(user_tom.name, "has an account balance of", user_tom.show_balance())


















