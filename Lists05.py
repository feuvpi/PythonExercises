## Build a little program that can read various number inputs and organize them into a list. Then the program should create
## two new separates list for even and odd numbers.

listItems = []
continueProgram = True
while True:
    listItems.append(int(input('Please enter a number: ')))
    answer = str(input('do you want to continue? Type N ir n for No: '))
    if answer in 'Nn':
        break


odds = []
evens = []

for number in listItems:
    if number % 2 == 0:
        evens.append(number)
    else:
        odds.append(number)
evens.sort()
odds.sort()
print('-'* 15)
print('Even values:')
print(evens)
print('-'* 15)
print('Odd values:')
print(odds)