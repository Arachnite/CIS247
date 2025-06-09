
# Brandon Jun
# Lab #3

"""
Check if three angles can form a valid triangle.

Args:
    angle1 (int): The first angle in degrees
    angle2 (int): The second angle in degrees
    angle3 (int): The third angle in degrees

Returns:
    bool: True if angles form a valid triangle, False if not

"""
def is_valid_triangle(angle1, angle2, angle3):

    # Check if sum equals exactly 180 degrees
    if angle1 + angle2 + angle3 != 180:
        return False

    return True

"""
Determine the type of triangle based on its angles.

Args:
    angle1, angle2, angle3: The three angles in degrees

Returns:
    str: 'acute', 'right', 'obtuse', or 'invalid'
    
"""
def get_triangle_type(angle1, angle2, angle3):

    if not is_valid_triangle(angle1, angle2, angle3):
        return 'invalid'

    if angle1 == 90 or angle2 == 90 or angle3 == 90:
        return 'right'

    if angle1 > 90 or angle2 > 90 or angle3 > 90:
        return 'obtuse'

    return 'acute'

"""
Get a positive integer from user input with validation.

Args:
    prompt (str): The prompt message

Returns:
    int: A positive integer/degree
"""
def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive degree.")
        except ValueError:
            print("Please enter a valid degree.")


# Program's User Interface
try:
    print("=== Triangle Angle Classifier ===")
    print("Enter three angles in degrees to check if they form a valid triangle.\n")

    # Get three angles from user
    angle1 = get_positive_integer("Enter the first angle (degrees): ")
    angle2 = get_positive_integer("Enter the second angle (degrees): ")
    angle3 = get_positive_integer("Enter the third angle (degrees): ")

    print(f"\nAngles entered: {angle1}°, {angle2}°, {angle3}°")
    print(f"Sum of angles: {angle1 + angle2 + angle3}°")

    if is_valid_triangle(angle1, angle2, angle3):
        print("✓ These angles can form a valid triangle!")

        triangle_type = get_triangle_type(angle1, angle2, angle3)

        if triangle_type == 'acute':
            print("Triangle type: Acute Triangle")
        elif triangle_type == 'right':
            print("Triangle type: Right Triangle")
        elif triangle_type == 'obtuse':
            print("Triangle type: Obtuse Triangle")

    else:
        print("✗ These angles cannot form a valid triangle.")

        if angle1 <= 0 or angle2 <= 0 or angle3 <= 0:
            print("Issue: All angles must be positive integers.")
        elif angle1 + angle2 + angle3 != 180:
            print("Issue: The sum of angles must be exactly 180 degrees.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")