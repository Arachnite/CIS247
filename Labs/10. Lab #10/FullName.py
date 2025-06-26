
# Brandon Jun
# Lab #10

class FullName:

    """
    Class to represent the person's full name

    Args:
        first_name (str): The first name of the person
        last_name (str): The last name of the person

    Returns:
        None
    """

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    """
    Return the full name
    
    Args:
        None
        
    Returns:
        str: The full name, First Last
    """

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    """
    Compare the two FullName objects
    
    Args:
        other (FullName): Another FullName object to compare with
        
    Returns:
        bool: True if self is greater than other, False otherwise
    """

    def __gt__(self, other):

        if self.last_name > other.last_name:
            return True
        elif self.last_name < other.last_name:
            return False
        else:
            return self.first_name > other.first_name