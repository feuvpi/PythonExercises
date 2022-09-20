# Write a program that helps a LOTTO player to create guesses.
# The program will ask how many games will be generated and will draw 6 numbers between 1 and
# 60 for each game, registering everything in a composite list.

from random import randint
from time import sleep

games = (int(input('How many Lotto games do you want to generate? ')))

cont = 0
set = []

print('----- LOTTO GAMES -----')
while(games > 0):
    set = []
    while True:
        num = randint(1,60)
        if num not in set:
            set.append(num)
        if(len(set) >= 6):
            break
    sleep(.7)
    print('---' * 10)
    print(set)
    games -= 1
print('---' * 10)
print('--- GOOD LUCK! ---')



