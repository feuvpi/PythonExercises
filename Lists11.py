
temp = []
princ = []

max = min = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        max = min = temp[1]
    else:
        if temp[1] > max:
            max = temp[1]
        if temp[1] < min:
            min = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break;


print('---' * 15)
print(f'Os dados foram {princ} ')
print(f'{len(princ)} pessoas foram cadastradas.')

print(f'O maior peso cadastrado foi {max}. Peso de:')
for p in princ:
    if p[1] == max:
        print(f'{p[0]}')
print(f'O menor peso cadastrado foi {min}. Peso de:')
for p in princ:
    if p[1] == min:
        print(f'{p[0]}')