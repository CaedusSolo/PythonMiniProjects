choice = "yes"   
while choice.lower() == "yes":
    while True:
        print('''
            888                                                          
            888                                                          
            888                                                          
            888888888d888 .d88b.  8888b. .d8888b 888  888888d888 .d88b.  
            888   888P"  d8P  Y8b    "88b88K     888  888888P"  d8P  Y8b 
            888   888    88888888.d888888"Y8888b.888  888888    88888888 
            Y88b. 888    Y8b.    888  888     X88Y88b 888888    Y8b.     
            "Y888888     "Y8888 "Y888888 88888P' "Y88888888     "Y8888 ''') 

        print("Welcome to this 'Choose Your Own Adventure' game!")
        print("Your task is to find the treasure.")

        firstChoice = input("You're at a crossroad. Which way do you choose to go? Type \"left\" or \"right\". : ").lower()

        while firstChoice != "left" and firstChoice != "right":
            firstChoice = input("You're at a crossroad. Which way do you choose to go? Type \"left\" or \"right\". : ").lower()

        if firstChoice == "right":
            print("You fell into a hole. Game over.")
            break

        elif firstChoice == "left": 
            print("You successfully evaded the monster lurking around! Onto the next challenge!")

        secondChoice = input("You see two paths, a river and a bridge. Which route do you take? Type 'river' or 'bridge'. : ").lower()
                
        while secondChoice != "river" and secondChoice != "bridge":
            secondChoice = input("You see two paths, a river and a bridge. Which route do you take? Type 'river' or 'bridge'. : ").lower()

        if secondChoice == "bridge":
            print("You successfully dodged the shark. Onto the next challenge!")
                    
        elif secondChoice == "river":
            print("You were eaten by a shark. Game over.")
            break 

        thirdChoice = input("You reach two houses, you desperately need to drink water. Which house do you go to for help? Type 'left' or 'right': ")

        while thirdChoice != "left" and thirdChoice != "right":
            thirdChoice = input("You reach two houses, you desperately need to drink water. Which house do you go to for help? Type 'left' or 'right': ")

        if thirdChoice == "right":
            print("The homeowner gave you some water and guided you to the treasure! You win!")
            break
                
        elif thirdChoice == "left":
            print("The homeowner was not so pleasant and poisoned you. Game over.")
            break 

    choice = input("Would you like to replay? Type 'yes' or 'no': ").lower()
    if choice != "yes":
        break
