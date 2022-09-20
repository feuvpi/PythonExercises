# Write a program that reads 5 numeric values and stores them in a list. At the end, show which was
# the highest and lowest value entered and their respective positions in the list.

list = [int(input('Enter an int: ')), int(input('Enter an int: ')), int(input('Enter an int: ')),
        int(input('Enter an int: ')), int(input('Enter an int: ')),]

print('-'*15)
print(f'The list entered is: {list}')
print('-'*15)
print(f'The higest value was {max(list)} and its index is {list.index(max(list))}')
print('-'*15)
print(f'The lowest value was {min(list)} and its index is {list.index(min(list))}')
