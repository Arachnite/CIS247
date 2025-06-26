
# Brandon Jun
# Homework #3

import os
import sys

"""
Create scores.txt file if it doesn't exist

Args:
    None
    
Returns:
    None
    
"""

def create_scores_file():

    if not os.path.exists('scores.txt'):
        with open('scores.txt', 'w') as file:
            pass

"""
Allows the user to view all scores recorded in scores.txt.

Args:
    None

Returns:
    None
    
"""

def view_scores():

    try:
        with open('scores.txt', 'r') as file:
            lines = file.readlines()

        if not lines:
            print("No scores recorded yet.")
            return

        for line in lines:
            line = line.strip()
            if line:
                parts = line.split()
                month = parts[0]
                day = parts[1]
                scores = parts[2:]

                if len(scores) == 1:
                    score_text = scores[0]
                elif len(scores) == 2:
                    score_text = f"{scores[0]} and {scores[1]}"
                else:
                    score_text = ", ".join(scores[:-1]) + f", and {scores[-1]}"

                print(f"On {month} {day}, you scored {score_text}")

    # except cases for errors while reading the file
    except FileNotFoundError:
        print("No scores file found. Please add some scores first.")
    except Exception as e:
        print(f"Error reading scores: {e}")

"""
Check if scores already exist for the given date

Args:
    month (str): Month of the scores
    day (str): Day of the scores
    
Returns:
    bool: True if scores exist for the date, False otherwise
    
"""

def score_exists_for_date(month, day):

    try:
        with open('scores.txt', 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split()
                    if len(parts) >= 2 and parts[0] == month and parts[1] == day:
                        return True
        return False
    except FileNotFoundError:
        return False
    except Exception:
        return False

"""
Add the new score to scores.txt

Args:
    None
    
Returns:
    None
    
"""

def add_score():

    month = input("Enter month: ").strip()

    try:
        day = int(input("Enter day (1-31): "))
        if day < 1 or day > 31:
            print("Error: Day must be between 1 and 31.")
            return
    except ValueError:
        print("Error: Please enter a valid number for the day.")
        return

    day_str = str(day)

    if score_exists_for_date(month, day_str):
        print("A set of scores already exists for this date.")
        return

    scores = []
    print("Enter scores (press Enter with no input to finish):")

    while True:
        score_input = input("Enter score (0-300): ").strip()

        if score_input == "":
            break

        try:
            score = int(score_input)
            if score < 0 or score > 300:
                print("Error: Score must be between 0 and 300.")
                continue
            scores.append(str(score))
        except ValueError:
            print("Error: Please enter a valid number.")
            continue

    if not scores:
        print("No scores entered.")
        return

    # Append to file
    try:
        with open('scores.txt', 'a') as file:
            line = f"{month} {day_str} {' '.join(scores)}\n"
            file.write(line)
        print("Scores added successfully!")
    except Exception as e:
        print(f"Error saving scores: {e}")

"""
Calculate the average of all scores

Args:
    None
    
Returns:
    float: Average score, or 0 if no scores are available or an error occurs
    
"""

def average_scores():

    try:
        total_score = 0
        total_count = 0

        with open('scores.txt', 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split()
                    # Skip month and day, process scores
                    scores = parts[2:]
                    for score in scores:
                        try:
                            total_score += int(score)
                            total_count += 1
                        except ValueError:
                            continue

        if total_count == 0:
            return 0

        return total_score / total_count

    except FileNotFoundError:
        return 0
    except Exception:
        return 0

"""
Count the number of perfect scores

Args:
    None
    
Returns:
    int: The number of perfect scores, or 0 if no scores are available or an error occurs
    
"""

def num_300s():

    try:
        count_300s = 0

        with open('scores.txt', 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split()
                    # Skip month and day, process scores
                    scores = parts[2:]
                    for score in scores:
                        try:
                            if int(score) == 300:
                                count_300s += 1
                        except ValueError:
                            continue

        return count_300s

    # except cases for errors while counting the number of perfect scores
    except FileNotFoundError:
        return 0
    except Exception:
        return 0


try:
    print("Bowling Scores Tracker")
    print("=" * 30)

    # Create scores.txt file if it doesn't exist
    create_scores_file()

    while True:
        print("\nOptions:")
        print("1. Quit the program")
        print("2. View all Scores")
        print("3. Add a Score")
        print("4. Average Scores")
        print("5. Number of 300s")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == '1':
            print("Goodbye!")
            sys.exit()

        elif choice == '2':
            view_scores()

        elif choice == '3':
            add_score()

        elif choice == '4':
            avg = average_scores()
            if avg == 0:
                print("No scores available to calculate average.")
            else:
                print(f"Average score: {avg:.2f}")

        elif choice == '5':
            count = num_300s()
            if count == 0:
                print("No perfect scores (300) found.")
            else:
                print(f"Number of 300s: {count}")

        else:
            print("Invalid choice. Please enter 1-5.")

except Exception as e:
    print(f"An error occurred: {e}")