
# Brandon Jun
# Homework #4

class Date:

    """
    Constructor to create Date object
    """
    def __init__(self, day, month, year):
        self._day = day
        self._month = month
        self._year = year

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, value):
        self._day = value

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value):
        self._month = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value

    def __str__(self):
        return f"{self._month}/{self._day}/{self._year}"

    def __eq__(self, other):
        if isinstance(other, Date):
            return (self._day == other._day and
                    self._month == other._month and
                    self._year == other._year)
        return False