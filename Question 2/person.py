# =============================================================================
#                               PERSON CLASS
# =============================================================================
from queue import Full


class Person:
    """ Constructor """
    def __init__(self, name, gender, biography="", private=False):
        self.name = name                # The person's name
        self.gender = gender            # The person's gender
        self.biography = biography      # The person's biography
    
    def show_profile(self):
        return (
            f"Name: {self.name}\n"
            f"Gender: {self.gender}\n"
            f"Biography: {self.biography}"
        )

    """ Update the person's biography"""
    """ Parameter 1: new biography string """
    def update_biography(self, new_bio):
        self.biography = new_bio

    """ Return the person's details (for test)"""
    def __str__(self):
        return f"Person(name={self.name}, gender={self.gender})"