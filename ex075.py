# Develop a program that takes four input values and store it into a tuple.
# Show if and how many times the value "9" shows up
# Shows in what position is value "3", if any
# Shows the even numbers

# take four input values into a tuple
inputs = (int(input("Enter a number: ")), int(input("Enter a number: ")),  int(input("Enter a number: ")), int(input("Enter a number: ")))

# Show how if and how many times the number 9 appears
count = 0
print(inputs)
for number in inputs:
    print(number)
    if number == "9":
        print(number)
        count += 1
if count == 0:
    print("The tuple does not contains the value 9")
else:
    print(f'The value 9 appears in the tuple {count} times')

# Show in what positions is value 3, if any
start_index = 0
for number in inputs:
    if number == '3':
        index = inputs.index(number, start_index)
        print(f'There is a value 3 at index {index}')
        start_index = index + 1


# Show the even numbers
even_count = 0
for number in inputs:
    if number % 2 == 0:
        print(number)






