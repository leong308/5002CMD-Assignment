# from person import Person

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
        for vertex in self.adj_list:
            if vertex.get_name() == name:
                return True
        return False

    def get_vertex_from_id(self, id):
        vertices = list(self.adj_list.keys())  # Convert to list to allow indexing
        try:
            vertex = vertices[id - 1]
            return vertex
        except Exception as e:
            print(f"❗ An error occurred while fetching this vertex: {e}")
            return None

    def get_vertex_from_name(self, name):
        for vertex in self.adj_list:
            if vertex.get_name() == name:
                return vertex
        return None  # If not found

    def get_total_vertices(self):
        return len(self.adj_list)

    """ Add a new vertex (person) """
    """ Parameter 1: vertex (person) class object """
    def add_vertex(self, vertex):
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
        for linkings in self.adj_list.values():
            # Check if the target vertex exists
            if vertex in linkings:
                # Remove the vertex from adjacency list
                linkings.remove(vertex)

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
    
    def get_incoming_edges(self, vertex):
        """Return a list of names of people who follow the given person name."""
        incoming = []
        for from_vertex, linkings in self.adj_list.items():
            for to_vertex in linkings:
                if to_vertex == vertex:
                    incoming.append(from_vertex.get_name())
        return incoming

    def get_outgoing_edges(self, vertex):
        """Return a list of names of people the given person name is following."""
        outgoing = []
        if vertex in self.adj_list:
            for to_vertex in self.adj_list[vertex]:
                outgoing.append(to_vertex.get_name())
        return outgoing

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

    def get_bidirectional_edges(self):
        bidirectional_edges = []
        for vertex1 in self.adj_list:
            for vertex2 in self.adj_list:
                # Avoid checking with own vertex
                if vertex1 != vertex2:
                    # Check whether there are edges in both incoming and outgoing
                    if (self.has_edge(vertex1, vertex2) and self.has_edge(vertex2, vertex1)):
                        # Make sure the vertices pair is not being recorded before in flipped side
                        if (vertex2, vertex1) not in bidirectional_edges:
                            # Record the vertices pair into the list
                            bidirectional_edges.append((vertex1, vertex2))
        return bidirectional_edges