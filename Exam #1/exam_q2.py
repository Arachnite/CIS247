
# Brandon Jun
# Exam #1, Question 2

import random

"""
Collects the user's guess

Args:
    None

Returns:
    int: The user's guess
"""

def get_user_guess():

    while True:
        try:
            guess = int(input("Enter your guess (1-6): "))
            if 1 <= guess <= 6:
                return guess
            print("Please enter a number between 1 and 6.")
        except ValueError:
            print("Please enter a number between 1 and 6.")

"""
Rolls a die 1-6

Args:
    None
    
Returns:
    int: The outcome of the roll
"""

def roll_die():

    return random.randint(1, 6)


def main():

    results = []
    correct_count = 0

    print()
    print("=" * 36)

    # For loop for 10 rolls
    for roll_num in range(1, 11):
        print(f"\nRoll {roll_num}:")
        guess = get_user_guess()
        outcome = roll_die()
        is_correct = guess == outcome

        if is_correct:
            correct_count += 1

        results.append((roll_num, guess, outcome, "Y" if is_correct else "N"))

    # Display results
    print("\nRoll      Guess    Outcome   Correct")
    print("-" * 36)
    for roll_num, guess, outcome, correct in results:
        print(f"{roll_num:<10}{guess:<9}{outcome:<10}{correct}")

    percentage = (correct_count / 10) * 100
    print(f"\nDisplay % Correct: {percentage}%")


if __name__ == "__main__":
    main()