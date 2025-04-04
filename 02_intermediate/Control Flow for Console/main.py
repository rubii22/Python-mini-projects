# Problem: High Low

# We want you to gain more experience working with control flow and Booleans in Python. To do this, we are going to have you develop a game! The game is called High-Low and the way it's played goes as follows:

# Two numbers are generated from 1 to 100 (inclusive on both ends): one for you and one for a computer, who will be your opponent. You can see your number, but not the computer's!
# You make a guess, saying your number is either higher than or lower than the computer's number
# If your guess matches the truth (ex. you guess your number is higher, and then your number is actually higher than the computer's), you get a point!

# Solution

import random

# Function to play one round of High-Low game
def high_low_game():
    rounds = int(input("Enter the number of rounds: "))  # Number of rounds in the game
    
    score = 0  # Initialize score
    for round_num in range(1, rounds + 1):
        # Generate random numbers for you and the computer
        your_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)
        
        # Show your number to the player
        print(f"\nRound {round_num}:")
        print(f"Your number is: {your_number}")
        
        # Ask the player to guess if their number is higher or lower than the computer's number
        guess = input("Is your number higher or lower than the computer's number? (Enter 'higher' or 'lower'): ").lower()
        
        # Determine if the player's guess was correct
        if (guess == 'higher' and your_number > computer_number) or (guess == 'lower' and your_number < computer_number):
            print(f"Correct! The computer's number was {computer_number}.")
            score += 1  # Increment score if correct
        else:
            print(f"Incorrect! The computer's number was {computer_number}.")
    
    # Print final score after all rounds are played
    print(f"\nGame over! Your final score is: {score} out of {rounds}")

# Call the function to start the game
high_low_game()
