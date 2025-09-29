#Word Game is a knock-off version of a popular online word-guessing game.

import random

# Sample list of 5-letter words
word_list = [
    "apple", "brave", "crane", "drape", "flame",
    "grape", "heart", "plane", "shark", "stone"
]

def inWord(letter, word):
    """Return True if letter is anywhere in word, else False."""
    return letter in word

def inSpot(letter, word, spot):
    """Return True if letter is at the specified spot (0-indexed) in word, else False."""
    return word[spot] == letter

def rateGuess(myGuess, word):
    """
    Returns a string representing feedback on myGuess compared to word.
    - Capital letter if letter is correct and in the right spot.
    - Lowercase letter if letter is in the word but in the wrong spot.
    - '.' if letter is not in the word.
    """
    result = []
    # To handle multiple occurrences, track counts of letters in the word
    word_letter_counts = {}
    for c in word:
        word_letter_counts[c] = word_letter_counts.get(c, 0) + 1

    # First pass: mark correct spots and decrease count
    correct_spots = [False] * len(word)
    for i in range(len(myGuess)):
        if inSpot(myGuess[i], word, i):
            result.append(myGuess[i].upper())
            correct_spots[i] = True
            word_letter_counts[myGuess[i]] -= 1
        else:
            result.append(None)  # placeholder for now

    # Second pass: check letters that are in the word but wrong spot
    for i in range(len(myGuess)):
        if result[i] is None:
            letter = myGuess[i]
            if letter in word: 
                (letter, word) and word_letter_counts.get(letter, 0) > 0
                result[i] = letter.lower()
                word_letter_counts[letter] -= 1
            else:
                result[i] = '.'

    return ''.join(result)

def main():
    word = random.choice(word_list)
    tries = 6
    print("Welcome to the Word Game! Guess the 5-letter word.")

    for attempt in range(tries):
        guess = input(f"Attempt {attempt+1}/{tries}: ").lower()
        if len(guess) != 5:
            print("Please enter a 5-letter word.")
            continue

        feedback = rateGuess(guess, word)
        print(feedback)

        if guess == word:
            print(f"Congratulations! You guessed the word '{word}' correctly in {attempt+1} tries.")
            break
    else:
        print(f"Sorry, you've used all {tries} attempts. The word was '{word}'.")

if __name__ == "__main__":
    main()


if __name__ == '__main__':
  main()
