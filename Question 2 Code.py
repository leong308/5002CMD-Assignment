# =============================================================================
#                             HASH TABLE CLASS
# =============================================================================

class SocialMedia:
    """ Constructor """
    def __init__(self):
        self.adj_list = dict()  # Create a dictionary as a member of the Person class

    """ Add a new vertex (person) into graph """
    """ Parameter 1: vertex (person) name """
    def addVertex(self, vertex):
        # Check if vertex already exists
        if vertex not in self.adj_list:
            # Add a new vertex with an empty neighbor list to the graph
            self.adj_list[vertex] = []

    """ Add an edge to connect between 2 vertices in a direction (Eg. following a person) """
    """ Parameter 1: first vertex (person who follows) name """
    """ Parameter 2: second vertex (person being followed) name """
    def add_edge(self, from_vertex, to_vertex):
        # Check if both vertices are in the graph
        if from_vertex in self.adj_list and to_vertex in self.adj_list:
            # Add an edge
            self.adj_list[from_vertex].append(to_vertex)
        else:
            raise ValueError("One or both vertices are not found in the graph")

    """ Print out the graph in list format """
    def print_adj_list(self):
        # Displays graph in adjacency list format
        for vertex in self.adj_list:
            print(f"{vertex.name} -> {self.adj_list[vertex.name]}")

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

def main():
    socialMedia = SocialMedia()
    person1 = Person('Leong Zi Qi', 'Male', '', False)

    socialMedia.addVertex(person1)

    # socialMedia.print_adj_list()

# =============================================================================
#                           PROGRAM LAUNCHES HERE
# =============================================================================

if __name__ == "__main__":
    main()