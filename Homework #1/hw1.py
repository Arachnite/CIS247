
# Brandon Jun
# Homework #1

def print_prices():
    print("\n" + "=" * 50)
    print("          MOVIE THEATER SEATING CHART")
    print("=" * 50)
    print("        | Seat Level  | Price per Ticket |")
    print("        |-------------|------------------|")
    print("        | Premium     |      $20.00      |")
    print("        | Standard    |      $12.00      |")
    print("        | Economy     |      $8.00       |")
    print("=" * 50)
    print()

def get_ticket_count(seat_type):
    while True:
        try:
            count = int(input(f"Enter the number of {seat_type} tickets: "))
            if count >= 0:
                return count
            else:
                print("Error: Please enter a non-negative integer.")
        except ValueError:
            print("Error: Please enter a valid integer.")

def print_totals():
    print("\n" + "=" * 50)
    print("                 TICKET RECEIPT")
    print("=" * 50)
    print("        | Seat Level  |   Total Prices   |")
    print("        |-------------|------------------|")
    print(f"        | Premium     |      ${premium_cost:,.2f}      |")
    print(f"        | Standard    |      ${standard_cost:,.2f}      |")
    if economy_tickets_sold == 1:
        print(f"        | Economy     |      ${economy_cost:,.2f}       |")
    else:
        print(f"        | Economy     |      ${economy_cost:,.2f}      |")
    print("        |-------------|------------------|")
    print(f"        | Total       |      ${total_cost:,.2f}      |")
    print("=" * 50)
    print()

try:
    PREMIUM_PRICE = 20.00
    STANDARD_PRICE = 12.00
    ECONOMY_PRICE = 8.00

    print_prices()

    premium_tickets_sold = get_ticket_count("Premium")
    standard_tickets_sold = get_ticket_count("Standard")
    economy_tickets_sold = get_ticket_count("Economy")

    premium_cost = premium_tickets_sold * PREMIUM_PRICE
    standard_cost = standard_tickets_sold * STANDARD_PRICE
    economy_cost = economy_tickets_sold * ECONOMY_PRICE
    total_cost = premium_cost + standard_cost + economy_cost

    print_totals()

except Exception as e:
    print(f"An unexpected error occurred: {e}")