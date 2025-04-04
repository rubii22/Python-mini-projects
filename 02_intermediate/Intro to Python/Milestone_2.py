# Milestone #2: Adding in All Planets

# Mars is not the only planet in our solar system with its own unique gravity. In fact, each planet has a different gravitational constant, which affects how much an object would weigh on that planet. Below is a list of the constants for each planet compared to Earth's gravity:

# Mercury: 37.6%
# Venus: 88.9%
# Mars: 37.8%
# Jupiter: 236.0%
# Saturn: 108.1%
# Uranus: 81.5%
# Neptune: 114.0%

# Write a Python program that prompts an Earthling to enter their weight on Earth and then to enter the name of a planet in our solar system. The program should print the equivalent weight on that planet rounded to 2 decimal places if necessary.
# You can assume that the user will always type in a planet with the first letter capitalized and you do not need to worry about the case where they type in something other than one of the above planets.

# Solution:

# Dictionary storing gravity factors for each planet
gravity_factors = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
}

# Function to calculate weight on a given planet
def planet_weight():
    # Prompt user for weight on Earth
    earth_weight = float(input("Enter your weight on Earth (in kg): "))
    
    # Prompt user for the planet name
    planet = input("Enter the name of a planet: ")

    # Check if the planet exists in our dictionary
    if planet in gravity_factors:
        # Calculate weight on the chosen planet
        new_weight = round(earth_weight * gravity_factors[planet], 2)
        print(f"Your weight on {planet} would be: {new_weight} kg")
    else:
        print("Invalid planet name. Please enter a valid planet.")

planet_weight()
