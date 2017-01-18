from random import choice
books = ('harry potter', 'percy jackson', 'legend', 'artemis fowl')
word = choice(books)
guesses_left = len(word)
correct = set()
incorrect = set()
name = input('What is your name?')
print(name,',', 'you have', guesses_left, 'left.')

while guesses_left:
    print('You have', guesses_left, 'guesses left.')
    result_list = [letter if letter in correct else '-' for letter in word]
    result = ''.join(result_list)
    if result == word:
      print(name, ', you won!')
    print(''.join(result))
    guess = input('What is your guess?')
    guesses_left -=1
    if guess in word:
        correct.add(guess)
        if guesses_left > 0:
            print('Game Over. You failed to solve this hangman,', name, 'Try again, if you dare.')
        if guesses_left < 0:
            print('You are correct. Please continue.')
