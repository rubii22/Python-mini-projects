# Problem Statement

# Write a simple joke bot. The bot starts by asking the user what they want. However, your program will only respond to one response: Joke.

# Solution

# Constants
PROMPT = "Hey there! What do you want? "
JOKE = """Alright, here’s a joke for you!  
Why don’t programmers like nature?  
Because it has too many bugs! 🐛😂"""
SORRY = "Oops! I can only tell jokes. Try asking for a joke!"

def joke_bot():
    user_input = input(PROMPT).strip() 
    if user_input.lower() == "joke": 
        print(JOKE)
    else:
        print(SORRY)

joke_bot()
