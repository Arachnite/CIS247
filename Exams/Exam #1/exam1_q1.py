
# Brandon Jun
# Exam #1, Question 1

"""
Collects the score of a player in a single game

Args:
    None

Returns:
    None
"""

def get_score():

    while True:
        try:
            score = int(input("Enter player's score for this game: "))

            if score >= 0:
                return score

            print("Your score cannot be negative. Please try again.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

"""
Calculates the average, highest, and lowest score

Args:
    scores (list): List of scores

Returns:
    tuple: Average, highest, and lowest score
"""

def perform_calculations(scores):

    average = sum(scores) / len(scores)
    high = max(scores)
    low = min(scores)
    return average, high, low


def main():

    print()
    try:
        while True:
            num_games = int(input("Enter the number of games played: "))
            if num_games > 0:
                break
            print("Number of games must be positive.")

        scores = []
        for i in range(num_games):
            score = get_score()
            scores.append(score)

        average, high, low = perform_calculations(scores)
        print("\nPlayer Statistics:")
        print(f"Average score: {average:.1f}")
        print(f"Highest score: {high}")
        print(f"Lowest score: {low}")

    except ValueError:
        print("Invalid input for number of games. Please enter a valid number.")


if __name__ == "__main__":
    main()