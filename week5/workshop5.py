import random
from tracemalloc import start, stop

# -------- TASK 1 --------
def guess_random_number(tries, start, stop):
    random_number = random.randint(start, stop) #chooses random number

    while tries != 0: #keeps going till tries are all gone
        for i in reversed(range(tries + 1)): #prints the remaining number of tries
            print("Number of tries left:", i)

            guess = int(input("Guess a number between 0 and 10:")) #user input

            if guess == random_number: #is guess correct
                print("You guessed the correct number!")
            elif guess < random_number: #guess is too low
                print("Guess higher!")
                tries -= 1
            elif guess not in range(start, stop):
                print("Enter a valid number between", start, " - ", stop)
            else:  #guess is too high
                print("Guess lower!")
                tries -= 1

            if tries == 0: #no more tries remaining = failure
                print("You have failed to guess the number", random_number)


#guess_random_number(5, 0, 10)

#--------TASK 2 --------

def guess_random_num_linear(tries, start, stop):
    random_number = random.randint(start, stop) #chooses random number
    print("The number for the program to guess is:", random_number)
    tries += 1


    for num in range(random_number + 1):
        print("The program is guessing...", num) #guess
        tries-= 1
        if tries == 0: #out of tries
            print("The program has failed to guess the correct number.")
            return
        elif num != random_number: #if wrong
            print("Number of tries left:", tries) 
        
        if num == random_number: #if correct
            print("The program has guessed the correct number!")  
            return

#guess_random_num_linear(5, 0, 10)

# -------- TASK 3 --------

def guess_random_num_binary(tries, start, stop):
    random_number = random.randint(start, stop) #chooses random number
    print("Random number to find:", random_number)
    low = start
    high = stop

    while tries > 0:
        mid = (low + high) // 2

        if mid == random_number:
            print("Found it!", mid)
            return
        if mid < random_number:
            print("Guess higher.")
            tries -= 1
            low = mid + 1
        if mid > random_number:
            print("Guess lower.")
            tries -=1
            high = mid - 1
    print("Your program failed to find the number.")


# guess_random_num_binary(5, 0, 100)






