import os 

art =    """             ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\
"""
print(art)
print("Welcome to this auction.")
bid_information = {}

def clear():
    if os.name == 'nt':   #Windows
        os.system('cls')
    else:
        os.system("clear")  #Mac and Linux

def prompt():
    name = input("What is your name?: ")
    bid_amount = int(input("What is your bid? : $"))
    bid_information.update({name : bid_amount})
    
    clear_or_not = input("Are there other bidders? Type 'yes' or 'no': ").lower()
    if clear_or_not == "yes":
        clear()
        prompt()
    else:
        return

prompt()

highest_bid = 0
highest_bidder = None

for key in bid_information:
    current_bid = bid_information.get(key)

    if current_bid > highest_bid:
        highest_bid = current_bid
        highest_bidder = key
    

print(f"The highest bid was ${highest_bid}, and it was made by {highest_bidder}!")