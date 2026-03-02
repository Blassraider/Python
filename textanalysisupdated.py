"""
Program: textanalysis.py
Debugging Exercise 4

Computes and displays the Flesch Index and the Grade
Level Equivalent for the readability of a text file.
Updated to count syllables containing multiple vowels
as single syllables.
"""
import os

# Take the inputs
fileName = input("Enter the file name: ")
if os.path.exists(fileName):
    with open(fileName, 'r') as inputFile:
        text = inputFile.read()

    # Count the sentences
    sentences = text.count('.') + text.count('?') + \
                text.count(':') + text.count(';') + \
                text.count('!')


    # Count the words
    words = len(text.split())

    # Count the syllables
    syllables = 0
    vowels = "aeiouAEIOU"
    for word in text.split():
        vowelSeen = False        # Corrects for multi-vowel syllables
        for character in word:
            if not vowelSeen and character in vowels:
                syllables += 1
                vowelSeen = True
            elif not character in vowels:
                vowelSeen = False
        for ending in ['es', 'ed', 'e']:
            if word.endswith(ending):
                syllables -= 1
        if word.endswith('le'):
            syllables += 1

    # Compute the Flesch Index and Grade Level
    index = 206.835 - 1.015 * (words / sentences) - \
            84.6 * (syllables / words)
    level = int(round(0.39 * (words / sentences) + 11.8 * \
                      (syllables / words) - 15.59))

    # Output the results
    print(f"The Flesch Index is: {index: .2f}")
    print(f"The Grade Level Equivalent is: {level}")
    print(f"- {sentences} sentences")
    print(f"- {words} words")
    print(f"- {syllables} syllables")

    # Rainy-Day scenario: file not found
else:
    print(f"Error: The file '{fileName}' was not found. Please check the path and try again.")
    

    


