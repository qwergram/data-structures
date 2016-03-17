# -*- coding: utf-8 -*-
"""Simple grpah construction.
Once you have a grasp of the basic idea, implement a simple graph (unweighted, directed) in Python. You may use any of the Python primitive data types that are available without importing any additional libraries (str, unicode, dict, list, tuple).

Your graph should support the following operations:

g.nodes(): return a list of all nodes in the graph
g.edges(): return a list of all edges in the graph
g.add_node(n): adds a new node ‘n’ to the graph
g.add_edge(n1, n2): adds a new edge to the graph connecting ‘n1’ and ‘n2’, if either n1 or n2 are not already present in the graph, they should be added.
g.del_node(n): deletes the node ‘n’ from the graph, raises an error if no such node exists
g.del_edge(n1, n2): deletes the edge connecting ‘n1’ and ‘n2’ from the graph, raises an error if no such edge exists
g.has_node(n): True if node ‘n’ is contained in the graph, False if not.
g.neighbors(n): returns the list of all nodes connected to ‘n’ by edges, raises an error if n is not in g
g.adjacent(n1, n2): returns True if there is an edge connecting n1 and n2, False if not, raises an error if either of the supplied nodes are not in g
Begin by creating a new branch “simple_graph” in your data-structures repository. For each method of your graph class (including the constructor), write tests first that demonstrates the functionality of that method, then implement the method to make the tests pass.

Focus on making small, atomic commits to git with well-written and meaningful commit messages.

Remember to update your README file with a description of this new data type as well as any additional sources, references or collaborations you may have used in completing the work.

"""

class SimpleGraph(object):
    """Defining simple graph class."""

    def _reset(self):
        self.graph_dict = {}

    def __init__(self):
        """Initialize Simple Graph object."""
        self._reset()

    def nodes(self):
        """Return a list of all nodes in the dict."""
        node_list = list(self.graph_dict.keys())
        return node_list

    def edges(self):
        """Return a list of all edges in the dict."""
        to_return = []
        for key in list(self.graph_dict.keys()):
            for value in self.graph_dict.get(key):
                to_return.append('{}-{}'.format(key, value))
        return to_return

    def add_node(self, node):
        """Add a new node 'n' to the graph."""
        self.graph_dict.setdefault(node, [])

    def add_edge(self, node1, node2):
        """Add a edge from node 1 to node 2."""
        self.add_node(node1)
        self.add_node(node2)
        self.graph_dict[node1].append(node2)

    def del_node(self, node):
        """Deletes the node from the graph."""
        try:
            del self.graph_dict[node]
            for key in self.graph_dict:
                if node in self.graph_dict[key]:
                    self.graph_dict[key].remove(node)
        except KeyError:
            raise ValueError('Node does not exist')

    def del_edge(self, node1, node2):
        """Deletes the edge connecting node 1 and node 2."""

    def has_node(self, node):
        """Return a boolean for if node exists."""

    def neighbors(self, node):
        """Return the list of all nodes connected to by edges."""

    def adjacent(self, node1, node2):
        """Return boolean for edges between two nodes."""
