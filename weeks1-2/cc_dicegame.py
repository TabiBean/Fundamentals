import random

def dice_game():
    while True:
        global high_score 
        high_score = 0
        print("Current High Score: ", high_score)
        print("1) Roll Dice")
        print("2) Leave Game")
        choice = input("Enter your choice: ")
    
        if choice == "1":
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            total_dice = dice1 + dice2
            print("You roll a...", dice1)
            print("You roll a...", dice2)
            print("You have rolled a total of:", total_dice)
        
            if total_dice > high_score:
                high_score = total_dice
                print("New high score!\n")
            else:
                print("Your high score is", high_score)
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            break

dice_game()
