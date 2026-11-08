"""
CP1404 Prac 06 – Guitars!
Estimated time: 20 minutes
Actual time: 33 minutes (start: 11:44, finish: 12:18)
"""
import datetime


class Guitar:
    """Guitar class."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise data used in class."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self) -> str:
        """Return string representation of class."""
        return f"{self.name} ({self.year}) : ${self.cost:10,.2f:.2f}"

    def get_age(self):
        """Return age of guitar."""
        return datetime.datetime.now().year - self.year

    def is_vintage(self):
        """Determine if guitar is considered vintage."""
        if self.get_age() > 50:
            return True
        return False
