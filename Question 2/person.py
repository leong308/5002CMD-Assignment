# =============================================================================
#                               PERSON CLASS
# =============================================================================
from queue import Full


class Person:
    """ Constructor """
    def __init__(self, name, gender, bio=""):
        self.name = name                # The person's name
        self.gender = gender            # The person's gender
        self.bio = bio   # The person's biography
    
    def show_profile(self):
        return (
            f"Name: {self.name}\n"
            f"Gender: {self.gender}\n"
            f"Biography: {self.bio}"
        )
    
    def get_name(self):
        return self.name
    
    def get_gender(self):
        return self.gender
    
    def get_bio(self):
        return self.biography
    
    def set_name(self, new_name):
        self.name = new_name
    
    def set_gender(self, new_gender):
        self.gender = new_gender

    """ Update the person's biography"""
    """ Parameter 1: new biography string """
    def set_bio(self, new_bio):
        self.bio = new_bio

    """ Return the person's details (for test)"""
    def __str__(self):
        return f"Person(name={self.name}, gender={self.gender})"