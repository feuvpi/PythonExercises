# create a programa that let user enter five numeric values and inset them into a list at the right position

listItems = []
item = 0
for item in range(0, 5):
    new_item = int(input('Please enter a number: '))
    if item == 0 or new_item > listItems[-1]:
        listItems.append(new_item)
    else:
        pos = 0
        while pos < len(listItems):
            if new_item <= listItems[pos]:
                listItems.insert(pos, new_item)
                break
            pos += 1

print('-+' * 15)
print(listItems)





