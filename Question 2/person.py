# =============================================================================
#                               PERSON CLASS
# =============================================================================
class Person:
    """ Constructor """
    def __init__(self, name, gender, biography="", private=False):
        self.name = name                # The person's name
        self.gender = gender            # The person's gender
        self.biography = biography      # The person's biography
        self.private = private          # The person's profile privacy status

    """ Check whether the profile is private """
    """ Return: True if private, False if public """
    def is_private(self):
        return self.private

    def show_profile(self):
        """Returns profile details if public, or limited message if private."""
        if not self.is_private():
            return (
                f"Name: {self.name}\n"
                f"Gender: {self.gender}\n"
                f"Biography: {self.biography}"
            )
        else:
            return "This profile is private."

    """ Update the person's biography"""
    """ Parameter 1: new biography string """
    def update_biography(self, new_bio):
        self.biography = new_bio

    """ Set the person's profile privacy """
    """ Parameter 1: True/False"""
    def set_privacy(self, private):
        self.private = private

    """ Return the person's details (for test)"""
    def __str__(self):
        return f"Person(name={self.name}, gender={self.gender}, privacy={self.private})"