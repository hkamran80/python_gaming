name = input('Hello. What is your name?')
print('Hello', name)
phrase = input('Please enter a phrase.')
vowels = ['a', 'e', 'i', 'o', 'u']
results = []

for letter in phrase:
    if letter not in vowels:
        results.append(letter)
print(''.join(results))
