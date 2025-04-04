#  Problem Statement

# Guess My Number

# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high
# Enter a new number: 25 Your guess is too low
# Enter a new number: 48 Congrats! The number was: 48

# Solution

import random

def guess_my_number():
    # Generate a random number between 0 and 99
    secret_number = random.randint(0, 99)
    attempts = 0 

    print("\n🎯 I am thinking of a number between 0 and 99...")
    
    while True:
        try:
            # Get user input
            guess = int(input("🔢 Enter your guess: "))
            attempts += 1  
            
            if guess > secret_number:
                print("📉 Too high! Try a smaller number.")
            elif guess < secret_number:
                print("📈 Too low! Try a bigger number.")
            else:
                print(f"🎉 Congrats! You guessed the number {secret_number} in {attempts} attempts!")
                break 
        
        except ValueError:
            print("⚠️ Invalid input! Please enter a valid number.")

guess_my_number()