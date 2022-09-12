# Create a program where the user can type seven numeric values and register them in a single list that keeps even and odd values ​​separate.
# At the end, show the even and odd values in ascending order.

# a list with two internal lists, for even and odd numbers
num = [[], []]

value = 0
for c in range(1,8):
    value = int(input('Enter a numeric value: '))
    if value % 2 == 0:
        num[0].append(value)
    else:
        num[1].append(value)

print("---" * 15)
print("Even values: ")
print(num[0])
print("---" * 15)
print("Odds values: ")
print(num[1])