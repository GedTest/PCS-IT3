word = "python"
print("Zahrajeme si takovou hru!")
print("Uhadnete moje slovo.")
print("NAPOVEDA: hadane slovo je programovaci jazyk!")

for i in word:
    print('_', end=' ')
print()

letterGuessed = ''
chances = len(word)
correct = 0
while (chances >= 0):
    print()

    guess = str(input("Zadejte svůj odhad: "))

    # Guess validation
    if not guess.isalpha():
        print("Prosim zadavejte jen pismena.")
        continue
    elif len(guess) > 1:
        print("Prosim zadejte pismena po jednom.")
        continue
    elif guess in letterGuessed:
        print("Tohle pismeno jste jiz uhadli")
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
        print("Prohral jsi....")
        break

    # Print word
    for char in word:
        if char in letterGuessed:
            print(char, end=' ')
            correct += 1
        else:
            print('_', end=' ')


