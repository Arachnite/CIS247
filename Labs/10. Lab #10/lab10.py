
# Brandon Jun
# Lab #10

from FullName import FullName

try:
    print("FullName Class Demonstration")
    print("=" * 40)

    person1 = FullName("Brandon", "Jun")
    person2 = FullName("William", "Lee")
    person3 = FullName("Allison", "Park")
    person4 = FullName("Alexander", "Kim")
    person5 = FullName("Isaac", "Chang")

    print("\n1. Demonstrating __str__ method:")
    print(f"Person 1: {person1}")
    print(f"Person 2: {person2}")
    print(f"Person 3: {person3}")
    print(f"Person 4: {person4}")
    print(f"Person 5: {person5}")

    print("\n2. Demonstrating __gt__ method:")

    print(f"\nComparing different last names:")
    print(f"{person1} > {person2}? {person1 > person2}")
    print(f"{person2} > {person1}? {person2 > person1}")
    print(f"{person4} > {person5}? {person4 > person5}")

    print(f"\nComparing same last names (different first names):")
    print(f"{person1} > {person3}? {person1 > person3}")
    print(f"{person3} > {person1}? {person3 > person1}")

    print(f"\nMore comparisons:")
    print(f"{person4} > {person2}? {person4 > person2}")
    print(f"{person5} > {person4}? {person5 > person4}")

    print("\n3. Demonstrating sorting with FullName objects:")
    people = [person1, person2, person3, person4, person5]

    print("Before sorting:")
    for i, person in enumerate(people, 1):
        print(f"  {i}. {person}")

    print("\nSorting using __gt__ method...")
    n = len(people)
    for i in range(n):
        for j in range(0, n - i - 1):
            if people[j] > people[j + 1]:
                people[j], people[j + 1] = people[j + 1], people[j]

    print("\nAfter sorting (alphabetical by last name, then first name):")
    for i, person in enumerate(people, 1):
        print(f"  {i}. {person}")

    print("\n4. Testing edge cases:")
    person6 = FullName("John", "Smith")
    print(f"Testing identical names:")
    print(f"{person1} > {person6}? {person1 > person6}")
    print(f"{person6} > {person1}? {person6 > person1}")

except Exception as e:
    print(f"An error occurred: {e}")