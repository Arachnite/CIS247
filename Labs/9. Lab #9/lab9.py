
# Brandon Jun
# Lab #9

"""
Collect city names and population

Args:
    None

Returns:
    None
"""

def get_city_data():
    cities = {}
    while True:
        city = input("\nEnter a city name (or press Enter to finish): ").strip()
        if not city:
            break

        try:
            population = int(input("Enter the population: "))
            if population < 0:
                print("Population cannot be negative. Please try again.")
                continue
            cities[city] = population
        except ValueError:
            print("Invalid population. Please enter a valid number.")
            continue

    return cities


try:
    print("Enter city names and populations")
    cities = get_city_data()

    large_cities = {city: pop for city, pop in cities.items() if pop > 2000000}

    print("\nCities with population over 2 million:")
    if large_cities:
        for city, population in large_cities.items():
            print(f"{city}: {population:,}")
    else:
        print("No cities found with population over 2 million.")

except Exception as e:
    print(f"An error occurred: {e}")