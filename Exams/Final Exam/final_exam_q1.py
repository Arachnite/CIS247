
# Brandon Jun
# Final Exam Question 1

# Import the Question class from Question.py
from Question import Question

def main():

    # Create the four astronomy related questions
    questions = [
        Question("What is the closest star to Earth (other than the Sun)?",
                 ["Sirius", "Proxima Centauri", "Alpha Centauri A", "Betelgeuse", "Vega"], 2),
        Question("Which planet in our solar system has the most moons?",
                 ["Jupiter", "Saturn", "Uranus", "Neptune", "Mars"], 2),
        Question("What type of celestial object is formed when a massive star collapses at the end of its life cycle?",
                 ["White Dwarf", "Neutron Star", "Red Giant", "Planetary Nebula", "Black Hole"], 5),
        Question("Which galaxy is on a collision course with the Milky Way?",
                 ["Triangulum Galaxy", "Large Magellanic Cloud", "Andromeda Galaxy", "Whirlpool Galaxy", "Sombrero Galaxy"], 3)
    ]

    # Initialize player scores
    player1_score = 0
    player2_score = 0

    print("Welcome to Astronomy Trivia!")

    # Loop through each question
    for i, question in enumerate(questions, 1):
        print(f"\nQuestion {i}:")
        print(question)

        try:
            p1_guess = int(input("Player 1, enter your answer (1-5): "))
            p2_guess = int(input("Player 2, enter your answer (1-5): "))

            p1_correct = question.check_answer(p1_guess)
            p2_correct = question.check_answer(p2_guess)

            print("\nResults:")
            if p1_correct:
                print("Player 1: Correct!")
                player1_score += 1
            else:
                print("Player 1: Incorrect")

            if p2_correct:
                print("Player 2: Correct!")
                player2_score += 1
            else:
                print("Player 2: Incorrect")

        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

    # Print final scores
    print(f"\nFinal Scores:")
    print(f"Player 1: {player1_score} points")
    print(f"Player 2: {player2_score} points")

if __name__ == "__main__":
    main()