
# Brandon Jun
# Homework #4

from Date import Date

class Event:

    """
    Constructor to create an Event object
    """
    def __init__(self, event_name, start_hour, end_hour, event_date):
        self._event_name = event_name
        self._start_hour = start_hour
        self._end_hour = end_hour
        self._event_date = event_date

    @property
    def event_name(self):
        return self._event_name

    @event_name.setter
    def event_name(self, value):
        self._event_name = value

    @property
    def start_hour(self):
        return self._start_hour

    @start_hour.setter
    def start_hour(self, value):
        if 0 <= value <= 23:
            self._start_hour = value
        else:
            raise ValueError("Start hour must be between 0 and 23")

    @property
    def end_hour(self):
        return self._end_hour

    @end_hour.setter
    def end_hour(self, value):
        if 0 <= value <= 23:
            self._end_hour = value
        else:
            raise ValueError("End hour must be between 0 and 23")

    @property
    def event_date(self):
        return self._event_date

    @event_date.setter
    def event_date(self, value):
        if isinstance(value, Date):
            self._event_date = value
        else:
            raise ValueError("Event date must be a Date object")

    def __str__(self):
        return f"Event: {self._event_name}, Time: {self._start_hour} to {self._end_hour}, Date: {self._event_date}"

    def overlaps_with(self, other_event):
        if self._event_date != other_event._event_date:
            return False

        return (self._start_hour < other_event._end_hour and
                other_event._start_hour < self._end_hour)