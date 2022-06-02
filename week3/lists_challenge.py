import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
    user_input = input("Press enter to pick a card, or type Q then enter to quit.")
    if user_input == "Q" or user_input == "q":
        break
    else:
        card_position = random.randrange(len(diamonds))
        card = diamonds[card_position]
        hand.append(card)
        diamonds.pop(card_position)

        print("Your card is: " + card)
        print("Remaining card: ", diamonds) 
        print("Your hand: ", hand)
        

if not diamonds:
    print("There are no more cards to pick.")       


        
