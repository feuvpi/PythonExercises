# Create a program that has a multi-word tuple (don't use accents). After that, you must show, for each word, what its vowels are.

words = ('plane', 'computer', 'brain', 'programming', 'python')

for word in words:
    print(f'At word {word} there is ', end='')
    for letter in word:
        if letter.lower() in 'aeiou':
            print(letter, end=', ')