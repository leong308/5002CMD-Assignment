# =============================================================================
#                               PERSON CLASS
# =============================================================================
from queue import Full


class Person:
    """ Constructor """
    """ Parameter 1: Person's name (string) """
    """ Parameter 2: Person's gender (string) """
    """ Parameter 3: Person's biography (string) - optional """
    def __init__(self, name, gender, bio=""):
        self.name = name        # The person's name
        self.gender = gender    # The person's gender
        self.bio = bio          # The person's biography
    
    """ Fetch all of the person's details in enhanced formatting """
    """ Return: String of person's details (stting) """
    def show_profile(self):
        return (
            f"Name: {self.name}\n"
            f"Gender: {self.gender}\n"
            f"Biography: {self.bio}"
        )
    
    """ Get the person's name """
    """ Return: Person's name (string) """
    def get_name(self):
        return self.name
    
    """ Get the person's gender """
    """ Return: Person's gender (string) """
    def get_gender(self):
        return self.gender
    
    """ Get the person's biography """
    """ Return: Person's biography (string) """
    def get_bio(self):
        return self.bio
    
    """ Set the new name """
    """ Parameter: New name (string) """
    def set_name(self, new_name):
        self.name = new_name
    
    """ Set the new gender """
    """ Parameter: New gender (string) """
    def set_gender(self, new_gender):
        self.gender = new_gender

    """ Set the new biography """
    """ Parameter: New biography (string) """
    def set_bio(self, new_bio):
        self.bio = new_bio

    """ Fetch the person's details (test) """
    """ Return: Person's details (string) """
    def __str__(self):
        return f"Person(name={self.name}, gender={self.gender})"