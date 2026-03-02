import os

# The Helper Functions

def count_sentences(text):
    """This counts the number of sentences in the text based on punctuation."""
    sentence_ending = ".?;:!"
    sentences = 0
    for char in text:
        if char in sentence_ending:
            sentences += 1
    return max(1, sentences)

def count_words(text):
    """This will split the text into words and returns the count."""
    word_list = text.split()
    return len(word_list), word_list

def count_syllables(word_list):
    """This will calculate the total syllables across a list of words."""
    syllables = 0
    vowels = "aeiouAEIOU"
    for word in word_list:
        vowel_seen = False
        for character in word:
            if not vowel_seen and character in vowels:
                syllables += 1
                vowel_seen = True
    
        
        for ending in ['es', 'ed', 'e']:
            if word.endswith(ending):
                syllables -= 1
        if word.endswith('le'):
            syllables += 1
            
    return max(len(word_list), syllables) # Make sure at least 1 per word

# The Main Functions

def main():
    """This contains the mainline logic which calls helper functions."""
    fileName = input("Enter the file name: ")

    # The error handling for file access
    if not os.path.exists(fileName):
        print(f"Error: The file '{fileName}' was not found.")
        return

    try:
        with open(fileName, 'r') as inputFile:
            text = inputFile.read()

        # Call helper functions
        sentences = count_sentences(text)
        words, word_list = count_words(text)
        syllables = count_syllables(word_list)

        # Calculations
        index = 206.835 - 1.015 * (words / sentences) - 84.6 * (syllables / words)
        level = int(round(0.39 * (words / sentences) + 11.8 * (syllables / words) - 15.59))

        # The output results
        print("-" * 30)
        print(f"The Flesch Index is: {index:.2f}")
        print(f"The Grade Level Equivalent is: {level}")
        print("-" * 30)
        print(f"Summary Statistics:")
        print(f" - {sentences} sentences")
        print(f" - {words} words")
        print(f" - {syllables} syllables")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
