import random 

print("Welcome to this rock paper scissors game!")

userChoice = input("Enter 0 for rock, 1 for paper, 2 for scissors. : ")
computer = random.choice([0,1,2])

if userChoice == "0":
    print("""Your choice: 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

    if computer == 0:
        print("""Computer's choice: 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""") 
        print("Tie!")
    
    elif computer == 1:
        print("""Computer's choice: 
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""") 
        print("Computer wins!")

    else:
        print("""Computer's choice: 
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
        print("You win!")

elif userChoice == "1":
    print("""Your choice: 
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""") 
    
    if computer == 0:
        print("""Computer's choice: 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""") 
        print("You win!")

    elif computer == 1:
        print("""Computer's choice: 
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""") 
        print("Tie!")

    else: 
        print("""Computer's choice: 
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
        print("Computer wins!")

elif userChoice == "2":
    print("""Your choice: 
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
    
    if computer == 0:
        print("""Computer's choice: 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""") 
        print("Computer wins!")

    elif computer == 1:
        print("""Computer's choice: 
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""") 
        print("You win!")

    else:
        print("""Computer's choice: 
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
        print("Tie!")

else: 
    print("Please enter 0, 1 or 2 only.")