import random

def hangman_game():
    word_list = ["python", "javascript", "java", "ruby", "php"]
    word = random.choice(word_list)
    guessed_letters = []
    attempts = 6
    display_word = "_" * len(word)

    print("Welcome to Hangman!")

    while attempts > 0:
        print(f"\nWord to guess: {display_word}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Remaining attempts: {attempts}")

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid letter.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed {guess}. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good job! {guess} is in the word.")
            display_word = "".join([letter if letter == guess or letter in guessed_letters else "_" for letter in word])
        else:
            attempts -= 1
            print(f"Oops! {guess} is not in the word.")
        
        if "_" not in display_word:
            print(f"\nCongratulations! You guessed the word: {word}")
            break
    else:
        print(f"\nGame Over! The word was: {word}")

hangman_game()
