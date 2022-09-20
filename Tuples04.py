## Create a little program thar has products and its prices stored in a tuple.
# At the end, show a price listing, organizing the data in tabular form.

products = ('bananas', 2.40, 'apples', 4.50, 'potatoes', 3.00, 'bread', 1.50)

print('-'*20)
print('Product Listing:')
print('-'*20)
for pos in range(0, len(products)):
    if pos % 2 == 0:
        print(f'{products[pos]:.<30}', end='')
    else:
        print(f'{products[pos]:>2}')

