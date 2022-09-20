# A program that take various number inputs and organize them in a lista.
# How many numbers were entered?
# List in descending order
# if number 5 was inserted or not

listItems = []
continueProgram = True
while True:
    listItems.append(int(input('Please enter a number: ')))
    print('Do you want to continue?')
    answer = str(input('do you want to continue? Type N ir n for No.'))
    if answer in 'Nn':
        break

print(f'You entered {len(listItems)} elements.')
print("--" * 15)
print('Entered list in descending order:')
listItems.sort(reverse=True)
print(listItems)
print('-' * 15)
if 5 in listItems:
    print('the value 5 is in ListItems')
else:
    print('The number 5 is not in ListItems')
