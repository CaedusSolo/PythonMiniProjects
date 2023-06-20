import os
import random 

possible_cards = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
card_values = {
    "A" : 11,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "10" : 10,
    "J" : 10,
    "Q" : 10,
    "K" : 10 
} 

artwork = """


.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      `------'                           |__/   

"""


def clear():
    if os.name == 'nt':   #Windows
        os.system('cls')
    else:
        os.system("clear")  #Mac and Linux 

def deal_card():
    card = random.choice(possible_cards)
    return card 

def calculate_total(cards):
    total = 0
    for card in cards:
        total += card_values.get(card)
    if "A" in cards and total > 21:
        total -= 10
    return total

def hit(playerCards,dealerCards,playerTotal,dealerTotal):            
    if input("Press 'y' to draw another card, press 'n' to pass: ") == "y":
        playerCards.append(deal_card())
        playerTotal = calculate_total(playerCards)
        print(f"Your cards: [ {', '.join(playerCards)} ], current total: {playerTotal}")
        print(f"Dealer's first card: {card_values.get(dealerCards[0])}")
        hit(playerCards,dealerCards,playerTotal,dealerTotal)

    else:
        print(f"Your final hand:  [ {', '.join(playerCards)} ] , final total: {playerTotal}")
        print(f"Dealer's final hand:  [ {', '.join(dealerCards) }] , final total: {dealerTotal}")

        if playerTotal > 21:
            print("You busted! You lose :( ")
        elif dealerTotal > 21:
            print("Dealer busted! You win! ")
        elif playerTotal > dealerTotal:
            print("Your hand beat the dealer's hand! You won! ")
        else:
            print("Dealer's hand beat yours! You lose :/ ")

        play()

def play():    #  to be displayed everytime user starts a game

    playerCards = []
    dealerCards = []
    playerTotal = 0
    dealerTotal = 0
    
    print(artwork) 

    if input("Would you like to play some Blackjack? Type 'y' or 'n': ").lower() == "y":

        clear()

        playerCards.extend([deal_card(),deal_card()])
        playerTotal = calculate_total(playerCards)

        dealerCards.extend([deal_card(),deal_card()])
        dealerTotal = calculate_total(dealerCards)
        
        if dealerTotal < 17:
            dealerCards.append(deal_card())
            dealerTotal = calculate_total(dealerCards)

        print(f"Your cards: {playerCards}, current total: {playerTotal}")
        print(f"Dealer's first card: {card_values.get(dealerCards[0])}")
        

    else:
        print("Well then, hope to see you around soon!")
        return 
    
    hit(playerCards,dealerCards,playerTotal,dealerTotal)

play()
