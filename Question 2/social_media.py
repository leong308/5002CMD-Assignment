# from person import Person

# =============================================================================
#                             SOCIAL MEDIA CLASS
# =============================================================================
class SocialMedia:
    """ Constructor """
    def __init__(self):
        self.adj_list = dict()  # Create a dictionary as a member of the Social Media class

    """ Check is the vertex is found """
    """ Parameter: vertex's name """
    """ Return: True if has vertex, False if no vertex """
    def has_vertex(self, name):
        # Loop through each vertex's key (vertex object)
        for vertex in self.adj_list:
            # Check if the vertex's name matches
            if vertex.get_name() == name:
                return True
        return False

    """ Fetch vertex using id count """
    """ Parameter: id count (int) """
    """ Return: vertex object (class) or None """
    def get_vertex_from_id(self, id):
        # Convert dictionary to list for indexing purpose
        # Only take the keys (vertex) into list, ignore items (neighbors)
        vertices = list(self.adj_list.keys())
        try:
            # Fetch the required vertex object and return
            vertex = vertices[id - 1]
            return vertex
        except Exception as e:
            print(f"❗ An error occurred while fetching this vertex id - [{id}]: {e}")
            # Return None if error occured or not found
            return None

    """ Fetch vertex using name """
    """ Parameter: name (string) """
    """ Return: vertex object (class) or None """
    def get_vertex_from_name(self, name):
        # Loop through each vertex's key (vertex object)
        try:
            for vertex in self.adj_list:
                # Check if the vertex's name matches
                if vertex.get_name() == name:
                    return vertex
        except Exception as e:
            print(f"❗ An error occurred while fetching this [{name}] vertex: {e}")
            # Return None if error occured
            return None
        # Return None if not found
        return None

    """ Fetch the amount of total existing vertices """
    """ Return: vertex count (int) """
    def get_total_vertices(self):
        return len(self.adj_list)

    """ Add a new vertex """
    """ Parameter: vertex object (class) """
    def add_vertex(self, vertex):
        # Check if vertex already exists
        # Check if already have 10 vertices
        if vertex not in self.adj_list and self.get_total_vertices() < 10:
            # Add a new vertex with an empty neighbor list to the graph
            self.adj_list[vertex] = []
    
    """ Remove a vertex (person) """
    """ Parameter: vertex object (class) """
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
        try:
            del self.adj_list[vertex]
        except Exception as e:
            print(f"❗ An error occurred while deleting vertex: {e}")
    
    """ Check is the edge direction exists """
    """ Parameter 1: first vertex object (class) """
    """ Parameter 2: second vertex object (class) """
    """ Return: True if edge found, False if no edge """
    def has_edge(self, from_vertex, to_vertex):
        # Return true if the edge is found in the graph
        if from_vertex in self.adj_list:
            # Check the from vertex's items (neighbors)
            # Return True if to vertex object is found in from vertex's items (neighbors)
            return to_vertex in self.adj_list[from_vertex]
        # Return False if not found
        return False
    
    """ Fetch all vertex/vertices that has this vertex in their items """
    """ Parameter: vertex object (class) """
    """ Return: All vertices names that has this vertex in their items (list) """
    def get_incoming_edges(self, vertex):
        incoming = []   # Create an empty list to store incoming vertices
        # Loop through each vertex's key (vertex object), items (neighbors)
        for from_vertex, linkings in self.adj_list.items():
            # Lopp through each vertex in the neighbors list
            for to_vertex in linkings:
                # When the target vertex (destination) is in the neighbors list
                if to_vertex == vertex:
                    # Append the name of the vertex into incoming list
                    try:
                        incoming.append(from_vertex.get_name())
                    except Exception as e:
                        print(f"❗ An error occurred while fetching incoming vertices for vertex [{vertex.get_name()}]: {e}")

        return incoming

    """ Fetch all vertex/vertices that this vertex have in its items """
    """ Parameter: vertex object (class) """
    """ Return: All vertices names that has this vertex in its items (list) """
    def get_outgoing_edges(self, vertex):
        outgoing = []   # Create an empty list to store incoming vertices
        # If target vertex is found in the dict
        if vertex in self.adj_list:
            # Loop through each vertex in the neighbors list
            for to_vertex in self.adj_list[vertex]:
                # Append the name of the vertex into outgoing list
                try:
                    outgoing.append(to_vertex.get_name())
                except Exception as e:
                    print(f"❗ An error occurred while fetching outgoing vertices for vertex [{vertex.get_name()}]: {e}")

        return outgoing

    """ Add an edge to connect between 2 vertices in 'a direction' only """
    """ Parameter 1: first vertex object (class) """
    """ Parameter 2: second vertex object (class)"""
    def add_edge(self, from_vertex, to_vertex):
        # Check if both vertices exists
        if from_vertex in self.adj_list and to_vertex in self.adj_list:
            # Add the to_vertex into from_vertex's items list (neighbors)
            try:
                self.adj_list[from_vertex].append(to_vertex)
            except Exception as e:
                print(f"❗ An error occurred while adding edge [{from_vertex.get_name()}] --> [{to_vertex.get_name()}]: {e}")
        else:
            print("One or both vertices are not found")

    """ Remove an edge direction between 2 vertices """
    """ Parameter 1: first vertex object (class) """
    """ Parameter 2: second vertex object (class)"""
    def remove_edge(self, from_vertex, to_vertex):
        # Check if first vertex exists
        if from_vertex in self.adj_list:
            # Check if second vertex in the first vertex's neighbors list
            if to_vertex in self.adj_list[from_vertex]:
                # Remove the to_vertex from from_vertex's items list (neighbors)
                try:
                    self.adj_list[from_vertex].remove(to_vertex)
                except Exception as e:
                    print(f"❗ An error occurred while removing edge [{from_vertex.get_name()}] --> [{to_vertex.get_name()}]: {e}")
            else:
                print("Edge does not exists")

    """ Fetch bi-directional edges between 2 vertices """
    """ Return: Vertices pairs that have bi-directional edges (list) """
    def get_bidirectional_edges(self):
        bidirectional_edges = []
        # Loop through all vertices from the list
        for vertex1 in self.adj_list:
            # Loop through all vertices from the list
            for vertex2 in self.adj_list:
                # Currently there will be vertex1 and vertex2 on hand
                # Avoid checking with own vertex
                if vertex1 != vertex2:
                    # Check whether there are edges in both incoming and outgoing
                    if (self.has_edge(vertex1, vertex2) and self.has_edge(vertex2, vertex1)):
                        # Make sure the vertices pair is not being recorded before in flipped side
                        if (vertex2, vertex1) not in bidirectional_edges:
                            # Record the vertices pair into the list as an item
                            bidirectional_edges.append((vertex1, vertex2))
                            
        return bidirectional_edges