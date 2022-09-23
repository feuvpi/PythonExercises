# Make a program that reads a student's name and average, also storing the situation in a dictionary.
# At the end, show the content of the structure on the screen.

student = dict()
student['name'] = str(input('Name: '))
student['mean'] = float(input(f'{student["name"]} mean: '))

if student['mean'] >= 7:
    student['situation'] = 'Aproved'
elif 5 <= student['mean'] < 7:
    student['situation'] = 'Finals'
else:
    student['situation'] = 'Reproved'
for k, v in student.items():
    print(f'{k} equals to {v}')