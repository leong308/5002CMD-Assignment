from person import Person

# =============================================================================
#                             SOCIAL MEDIA CLASS
# =============================================================================
class SocialMedia:
    """ Constructor """
    def __init__(self):
        self.adj_list = dict()  # Create a dictionary as a member of the Social Media class

    """ Check is the vertex (person) is found """
    """ Parameter 1: vertex (person) class object """
    """ Return: True if has vertex, False if no vertex """
    def has_vertex(self, name):
        # Loop through each person object in the graph
        for person in self.adj_list:
            if person.name == name:
                return True
        return False

    def get_total_vertices(self):
        return len(self.adj_list)

    """ Add a new vertex (person) """
    """ Parameter 1: vertex (person) class object """
    def addVertex(self, vertex):
        # Check if vertex already exists
        # Check if already have 10 vertices
        if vertex not in self.adj_list and self.get_total_vertices() < 10:
            # Add a new vertex with an empty neighbor list to the graph
            self.adj_list[vertex] = []
    
    """ Remove a vertex (person) """
    """ Parameter 1: vertex (person) class object """
    def remove_vertex(self, vertex):
        # Prompt error message if vertex is not in graph
        if vertex not in self.adj_list:
            raise ValueError(f"Target does not exists")     # Reusable message

        # Iterate through all the neighbors for every vertex
        for neighbors in self.adj_list.values():
            # Check if the target vertex exists
            if vertex in neighbors:
                # Remove the vertex from adjacency list
                neighbors.remove(vertex)

        # Remove the vertex from the graph
        del self.adj_list[vertex]
    
    """ Check is the edge (connection between 2 persons) is found """
    """ Parameter 1: first vertex (person) class object """
    """ Parameter 2: second vertex (person) class object """
    """ Return: True if has edge between, False if no edge between """
    def has_edge(self, from_vertex, to_vertex):
        # Return true if the edge is found in the graph
        if from_vertex in self.adj_list:
            return to_vertex in self.adj_list[from_vertex]
        return False

    """ Add an edge to connect between 2 vertices in a direction (Eg. following a person) """
    """ Parameter 1: first vertex (person who follows) class object """
    """ Parameter 2: second vertex (person being followed) class object """
    def add_edge(self, from_vertex, to_vertex):
        # Check if both vertices are in the graph
        if from_vertex in self.adj_list and to_vertex in self.adj_list:
            # Add an edge
            self.adj_list[from_vertex].append(to_vertex)
        else:
            raise ValueError("One or both vertices are not found in the graph")

    """ Remove an edge direction between 2 vertices (persons) """
    """ Parameter 1: first vertex (person) class object """
    """ Parameter 2: second vertex (person) class object """
    def remove_edge(self, from_vertex, to_vertex):
        # Check if first vertex is found in graph
        if from_vertex in self.adj_list:
            # Check if second vertex is found in graph
            if to_vertex in self.adj_list[from_vertex]:
                self.adj_list[from_vertex].remove(to_vertex)    # Remove edge
            else:
                raise ValueError("Edge does not exists")

    """ Print out the graph in list format """
    def print_adj_list(self):
        # Loop through each person
        for vertex in self.adj_list:
            names_list = []  # to store names of related people

            # Loop through and write the related person names into names_list
            for related in self.adj_list[vertex]:
                names_list.append(related.name)

            # Print the person's name and their connections
            print(vertex.name, "->", names_list)

    """ Print out the list of users """
    def print_all_users(self):
        count = 1
        # Loop through each person
        for vertex in self.adj_list:
            # Print the person's name 
            print(f"{count}. {vertex.name}")
            count += 1