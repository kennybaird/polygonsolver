"""Solve the Times Polygon Solver"""


def can_form_word(word, mandatory_letter, optional_letters, min_word_count):
    """Function to check if a word can be formed from the given letters"""
    if mandatory_letter not in word:
        return False

    required_letters = set(optional_letters + [mandatory_letter])

    for letter in word:
        if letter not in required_letters:
            return False
        required_letters.discard(letter)

    # Subtract 1 for the mandatory letter
    return len(optional_letters) - len(required_letters) >= min_word_count - 1


# Get word length
while True:
    try:
        min_word_count = int(input("Enter a number: "))
        break
    except ValueError:
        print("That's not an int!")
print(min_word_count)


# Get letters in anagrams
# Mandatory letter
while True:
    mandatory_letter = input("Enter mandatory letter: ")
    if mandatory_letter.isalpha() and len(mandatory_letter) == 1:
        break
    else:
        print("Please enter a single letter.")


# Other letters
optional_letters_dict = {}
while True:
    optional_letters = input("Enter other letters: ")
    if optional_letters.isalpha():
        for index, char in enumerate(optional_letters, start=1):
            optional_letters_dict[index] = char

        print("Resulting dictionary:", optional_letters_dict)
        break

# Dictionary found on GitHub - maybe open this file directly ?
# https://github.com/dwyl/english-words/blob/master/words_alpha.txt
file_name = "words_alpha.txt"
try:
    found_words = []
    with open(file_name, 'r') as file:
        for line in file:
            word = line.strip().lower()  # Get rid of newline characters and convert to lowercase
            if len(word) >= min_word_count and can_form_word(word, mandatory_letter,
                list(optional_letters_dict.values()), min_word_count):
                found_words.append(word)

    if found_words:
        print(
            f"Words found from combinations of letters"
            f"including '{mandatory_letter}' and {optional_letters_dict.values()})"
            f"with length at least {min_word_count}:")
        print(", ".join(found_words))
    else:
        print("No words found.")

except FileNotFoundError:
    print(f"File '{file_name}' not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
