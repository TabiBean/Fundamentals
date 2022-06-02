

#Login
def login(database, username, password): #Verifies log in
    if username in database.keys() and password == database[username]:
        print("\nWelcome back", username+"!")
        return username

    elif username in database.keys() and password not in database.values():
        #Incorrect password
        print("\nIncorrect password for: " , username )
        return ""

    else: #Incorrect username and password
        print("\nUser not found. Please register.")
        return ""

#Register
def register(database, username):
    if username in database.keys():
        print("\nUsername already registered.")
        return ""
    else:
        print("\nUsername", username, "registered!")
        return username
        





