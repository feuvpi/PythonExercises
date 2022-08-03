## Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.

## criando a tupla
cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('O numero precisa estar entre 0 e 20!')
print(f'Você digitou o numero {cont[num]}')

