import random

artwork = """

  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  

"""

print(artwork)
print("Welcome to this Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard' : ").lower()
random_number = random.randint(1,100)

if difficulty == "easy":
    lives = 10
    user_guess = False

    while not user_guess:
        print(f"You have {lives} attempt(s) remaining to guess the correct number.")
        guess = int(input("Enter your guess: "))

        if guess == random_number:
            print(f"You got it! The correct answer was {guess}! Well done!")
            user_guess = True

        else:
            lives -= 1
            if guess > random_number:
                print("Too high. Try again.")
            else:
                print("Too low. Try again.")
        
        if lives == 0:
            print(f"You ran out of lives. You lose. (Correct answer was {random_number})")
            break

else:
    lives = 5
    user_guess = False

    while not user_guess:
        print(f"You have {lives} attempt(s) remaining to guess the correct number.")
        guess = int(input("Enter your guess: "))

        if guess == random_number:
            print(f"You got it! The correct answer was {guess}! Well done!")
            user_guess = True

        else:
            lives -= 1
            if guess > random_number:
                print("Too high. Try again.")
            else:
                print("Too low. Try again.")
        
        if lives == 0:
            print(f"You ran out of lives. You lose. (Correct answer was {random_number})")
            break



