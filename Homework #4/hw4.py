
# Brandon Jun
# Homework #4

from Date import Date
from Event import Event

"""
To add an event

Args:
    events_list (list): List of Event objects to modify
    
Return:
    None
"""
def add_event(events_list):
    print("\n--- Add New Event ---")

    try:
        day = int(input("Enter day (1-31): "))
        month = int(input("Enter month (1-12): "))
        year = int(input("Enter year: "))

        start_hour = int(input("Enter start hour (0-23): "))
        end_hour = int(input("Enter end hour (0-23): "))

        if not (0 <= start_hour <= 23):
            print("Error: Start hour must be between 0 and 23")
            return
        if not (0 <= end_hour <= 23):
            print("Error: End hour must be between 0 and 23")
            return
        if start_hour >= end_hour:
            print("Error: Start hour must be less than end hour")
            return

        event_name = input("Enter event name: ").strip()
        if not event_name:
            print("Error: Event name cannot be empty")
            return

        event_date = Date(day, month, year)
        new_event = Event(event_name, start_hour, end_hour, event_date)

        for existing_event in events_list:
            if new_event.overlaps_with(existing_event):
                print("Error: Event overlaps with existing event:")
                print(f"  {existing_event}")
                print("New event not added.")
                return

        events_list.append(new_event)
        print("Event added successfully!")

    except ValueError:
        print("Error: Please enter valid numbers for date and time")

"""
To cancel an event

Args:
    events_list (list): List of Event objects to modify
    
Return:
    None
"""
def cancel_event(events_list):
    print("\n--- Cancel Event ---")

    if not events_list:
        print("No events to cancel.")
        return

    event_name = input("Enter the name of the event to cancel: ").strip()

    for i, event in enumerate(events_list):
        if event.event_name.lower() == event_name.lower():
            removed_event = events_list.pop(i)
            print(f"Event '{removed_event.event_name}' has been cancelled.")
            return

    print(f"Event '{event_name}' not found.")

"""
To view all events

Args:
    events_list (list): List of Event objects to display

Return:
    None
"""

def view_all_events(events_list):
    """Display all events in the events list"""
    print("\n--- All Scheduled Events ---")

    if not events_list:
        print("No events scheduled.")
        return

    for i, event in enumerate(events_list, 1):
        print(f"{i}. {event}")

try:
    print("Convention Center Scheduling System")
    print("=" * 40)

    events_list = []

    while True:
        print("\nMenu Options:")
        print("1. Add an Event")
        print("2. Cancel an Event")
        print("3. View All Events")
        print("4. Quit")

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == '1':
            add_event(events_list)

        elif choice == '2':
            cancel_event(events_list)

        elif choice == '3':
            view_all_events(events_list)

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")