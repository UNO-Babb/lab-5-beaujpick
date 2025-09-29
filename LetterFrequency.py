#LetterFrequency.py
#Name:
#Date:
#Assignment:

import csv
import string

def letter_frequency(message):
    # Initialize frequency list for 26 letters A-Z
    frequencies = [0] * 26

    # Normalize message to uppercase
    message = message.upper()

    for letter in message:
        if letter in string.ascii_uppercase:
            pos = ord(letter) - ord('A')
            frequencies[pos] += 1

    return frequencies

def save_to_csv(frequencies, filename="letter_frequencies.csv"):
    # Write frequencies to a CSV with columns: Letter, Frequency
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Letter", "Frequency"])

        for i in range(26):
            letter = chr(ord('A') + i)
            writer.writerow([letter, frequencies[i]])

def main():
    message = input("Enter a message to analyze letter frequency:\n")
    frequencies = letter_frequency(message)
    save_to_csv(frequencies)
    print(f"Letter frequency saved to 'letter_frequencies.csv'. Open this file in Excel to create your chart.")

if __name__ == "__main__":
    main()
