
# Brandon Jun
# Lab #4

"""
Get the amount of stores from user

Args:
    prompt (str): The prompt message

Returns:
    stores (int): The number of stores, must be greater than 0

"""
def get_stores(prompt):
    while True:
        try:
            stores = int(input(prompt))
            if stores > 0:
                return stores
            raise ValueError("Number of stores cannot be less than 1.")
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid number.")

"""
Gets the sales for each store from user

Args:
    None

Returns:
    sales_list (list, int): A list of sales for each store

"""
def get_sales():

    sales_list = []

    for store_num in range(1, num_stores + 1):
        while True:
            try:
                sales = int(input(f"Enter today's sales for store {store_num}: "))
                if sales >= 0:
                    sales_list.append(sales)
                    break
                else:
                    print("Please enter a non-negative number.")
            except ValueError:
                print("Please enter a valid integer.")

    return sales_list

"""
Print the sales bar chart for each store.

Args:
    None

Returns:
    None

"""
def print_sales_bar_chart():
    print("\nSALES BAR CHART (Each * = $100)")
    print("--------------------------------")
    for store_num, sales in enumerate(sales_list, 1):
        print(f"Store {store_num}: ", end = "")

        astricks = sales // 100  # Each '*' represents $100 in sales
        for i in range(astricks):
            print("*", end = "")
        print(f" - {astricks}")

        if store_num != num_stores:
            print("--------------------------------")

# Program's User Interface
try:
    num_stores = get_stores("\nHow many stores do you own? ")
    print("--------------------------------")

    sales_list = get_sales()

    print_sales_bar_chart()

except Exception as e:
    print(f"An error occurred: {e}")
