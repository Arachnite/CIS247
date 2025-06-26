
# Brandon Jun
# Lab #8

import sys

try:

    # Dictionary to store word -> list of line numbers
    word_dict = {}

    try:
        with open('quote.txt', 'r') as file:
            for line_num, line in enumerate(file, 1):
                line = line.strip().lower()

                words = line.split()

                for word in words:
                    if word in word_dict:
                        if line_num not in word_dict[word]:
                            word_dict[word].append(line_num)

                    else:
                        word_dict[word] = [line_num]

    except FileNotFoundError:
        print("Error: quote.txt file not found!")
        sys.exit()

    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit()

    # Print the dictionary data in the required format
    for word, line_numbers in word_dict.items():
        line_nums_str = ' '.join(map(str, line_numbers))
        print(f"{word} {line_nums_str}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")