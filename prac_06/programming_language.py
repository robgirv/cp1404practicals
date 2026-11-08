"""
Programming Language Intermediate Exercise Module.
Estimated time: 10 minutes
Start time: 11:22
Finish time: 11:38
Total time: 16 minutes (exceeded estimated time by 6 mins)
"""


class ProgrammingLanguage:
    """Programming Language class."""

    def __init__(self, name, typing, reflection, year):
        """Initialise data used in class."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self) -> str:
        """Returns string representation of class."""
        return f"{self.name}, {self.typing} Typing, Reflection={True}, First appeared in {self.year}"

    def is_dynamic(self):
        """Determine if language is dynamic."""
        if self.typing == "Dynamic":
            return True
        return False
