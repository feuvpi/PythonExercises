# Python Exercise 087: Improve the previous challenge by showing at the end:
# A) The sum of all even value entered.
# B) The sum of the values in the third column.
# C) The largest value of the second row.

matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

sumevens = max = sumcol = 0


for r in range(0,3):
    for c in range(0, 3):
        matrix[r][c] = int(input(f'Enter a number for position [{r}, {c}]: '))

print('---' * 15)
for r in range(0,3):
    for c in range(0,3):
        if matrix[r][c] % 2 == 0:
            sumevens += matrix[r][c]
        print(f'[{matrix[r][c]:^5}]', end='')
    print()

print('---' * 15)
print(f'A: The sum of all even values: {sumevens}')

print('---' * 15)

for r in range(0,3):
    sumcol += matrix[r][2]
print(f'B: The sum of third column values: {sumcol}')

print('---' * 15)

for c in range(0,3):
    if(matrix[1][c] > max):
        max = matrix[1][c]
print(f'C: The largest value of the second row: {max}')


