from numpy import random

# Working with tuplas
# Create a program that generates five random numbers and place them in a tupla.
# Show the created numbers and smallest and highest values

# Generate 5 Random numbers into a tupla
set = (f'{random.randint(100)}', f'{random.randint(100)}', f'{random.randint(100)}', f'{random.randint(100)}', f'{random.randint(100)}',)

# display created numbers
print("Generated values are:")
print(set)

# display minimum value
print("Minimum value is:")
print(min(set))

# display maximum value
print("Maximum value is:")
print(max(set))