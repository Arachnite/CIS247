
# Brandon Jun
# Lab #6

import os

try:
    os.makedirs('data', exist_ok=True)

    print()
    print("Multiplication Calculator")
    print("Enter two numbers to multiply, or 'quit' to exit")
    print("-" * 40)

    while True:
        try:
            first_input = input("Enter first number (or 'quit' to exit): ").strip()
            if first_input.lower() == 'quit':
                break

            second_input = input("Enter second number: ").strip()
            if second_input.lower() == 'quit':
                break

            num1 = float(first_input)
            num2 = float(second_input)

            product = num1 * num2

            if num1.is_integer():
                num1 = int(num1)
            if num2.is_integer():
                num2 = int(num2)
            if product.is_integer():
                product = int(product)

            equation = f"{num1} * {num2} = {product}"

            print(f"Result: {equation}")

            with open('data/results.txt', 'a') as file:
                file.write(equation + '\n')

            print("Result saved to data/results.txt")
            print()

        except ValueError:
            print("Please enter valid numbers!")
            print()
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            print()

except Exception as e:
    print(f"An error occurred while creating the directory: {e}")