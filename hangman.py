import random

words = ["python", "java", "computer", "programming", "developer"]

word = random.choice(words)

display = ["_"] * len(word)

wrong_guesses = 0

print("🎮 HANGMAN GAME")

while wrong_guesses < 6 and "_" in display:

    print("\nWord:", " ".join(display))

    guess = input("Enter a letter: ").lower()

    if guess in word:

        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess

        print("Good guess!")

    else:

        wrong_guesses += 1

        print("Wrong guess!")
        print("Remaining attempts:", 6 - wrong_guesses)


if "_" not in display:

    print("\nCongratulations! You guessed the word!")
    print("The word was:", word)

else:

    print("\nGame Over!")
    print("The word was:", word)