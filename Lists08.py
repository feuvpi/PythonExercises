# Create a program that declares a 3×3 dimensional matrix and fills it with values
# read from the keyboard. At the end, show the matrix on the screen, with the correct formatting.

matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for r in range(0,3):
    for c in range(0, 3):
        matrix[r][c] = int(input(f'Enter a number for position [{r}, {c}]: '))

print('---' * 15)
for r in range(0,3):
    for c in range(0,3):
        print(f'[{matrix[r][c]:^5}]', end='')
    print()

