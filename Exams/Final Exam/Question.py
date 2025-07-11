
# Brandon Jun
# Final Exam Question Class

class Question:
    """
    Constructor for the Question Class.

    Args:
        question_text (str): The text of the question.
        options (list): A list of 5 options for the question.
        answer_index (int): The index of the correct answer (0-4).

    Raises:
        ValueError: If options list does not contain exactly 5 items or if answer_index is not between 0 and 4.
    """

    def __init__(self, question_text, options, answer_index):
        if len(options) != 5:
            raise ValueError("Must provide exactly 5 options")
        if not 0 <= answer_index <= 4:
            raise ValueError("Answer index must be between 0 and 4")

        self.question_text = question_text
        self.options = options
        self.answer_index = answer_index

    """
    Returns a string representation of the question and its options.

    Args:
        None

    Returns:
        str: A formatted string containing the question and its options.
    """

    def __str__(self):
        result = f"{self.question_text}\n"
        for i, option in enumerate(self.options, 1):
            result += f"{i}. {option}\n"
        return result

    """
    Returns the question text.

    Args:
        None

    Returns:
        str: The text of the question.
    """

    def check_answer(self, guess):
        # Convert 1-based input to 0-based index
        return guess - 1 == self.answer_index