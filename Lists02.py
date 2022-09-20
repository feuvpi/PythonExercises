# Create a program where the user can enter several numeric values and register them in a list.
# If the number already exists in there, it will not be added.
# At the end, all unique values entered will be displayed, in ascending order

list = []
for item in range(0, 5):
    i = 1
    while i > 0:
        new_item = int(input('Please enter a number: '))
        if new_item in list:
            print("Can not repeat values. Digit again.")
        else:
            list.append(new_item)
            break
print('-'*15)
print('The entered values are:')
list.sort()
print(list)
