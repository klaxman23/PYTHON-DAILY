# This Python program calculates the length and weight of a person based on their height.

# Get the height of the person in inches.
height = float(input("Enter your height in inches: "))

# Calculate the length of the person in inches.
length = height * 0.65

# Calculate the weight of the person in pounds.
weight = height * 2.2

# Print the length and weight of the person.
print("Your length is", length, "inches.")
print("Your weight is", weight, "pounds.")