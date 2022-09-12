# Create a program that reads the name and two grades of several students and stores them all in a composite list.
# At the end, show a report card containing the average of each one and allow the user to show the grades of each student individually.

ficha = list()

while True:
    name = str(input('Name: '))
    grade1 = float(input('Grade 1: '))
    grade2 = float(input('Grade 2: '))
    mean = (grade1 + grade2) / 2
    ficha.append([name, [grade1, grade2], mean])
    cont = str(input('Do you want to continue? [Y/N]'))
    if cont in 'Nn':
        break
print('--*--' * 30)
print(f'{"No.":<4}{"NAME:":<10}{"MEAN:":>8}')
print('---'*15)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*45)
    opc = int(input('Choose a student to show grades. (999 ends program): '))
    if opc == 999:
        print('TERMINATING.')
        break
    if opc <= len(ficha) -1:
        print(f'{ficha[opc][0]}`s grades: {ficha[opc][1]}')
print('SESSION ENDED.')
