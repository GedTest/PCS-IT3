word = "python"
print('Guess the word! HINT: word is a name of a fruit')

for i in word:
    print('_', end=' ')
print()

letterGuessed = ''
chances = len(word)
correct = 0
while (chances >= 0):
    print()

    guess = str(input('Enter a letter to guess: '))

    # Guess validation
    if not guess.isalpha():
        print('Enter only a LETTER')
        continue
    elif len(guess) > 1:
        print('Enter only a SINGLE letter')
        continue
    elif guess in letterGuessed:
        print('You have already guessed that letter')
        continue

    # If letter is in word
    if guess in word:
        k = word.count(guess)
        for _ in range(k):
            letterGuessed += guess
    else:
        chances -= 1
        
    # Player lose
    if chances <= 0:
        print()
        print('You lost! Try again..')
        break

    # Print word
    for char in word:
        if char in letterGuessed:
            print(char, end=' ')
            correct += 1
        else:
            print('_', end=' ')


