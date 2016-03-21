# -*- coding: utf-8 -*-
"""Simple Graph structure."""


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
        """Delete the node from the graph."""
        try:
            del self.graph_dict[node]
            for key in self.graph_dict:
                if node in self.graph_dict[key]:
                    self.graph_dict[key].remove(node)
        except KeyError:
            raise KeyError('Node does not exist')

    def del_edge(self, node1, node2):
        """Delete the edge connecting node 1 and node 2."""
        try:
            self.graph_dict[node1].remove(node2)
        except KeyError:
            raise KeyError('Node1 does not exist')
        except ValueError:
            raise ValueError('Node2 does not exist')

    def has_node(self, node):
        """Return a boolean for if node exists."""
        return isinstance(self.graph_dict.get(node), list)

    def neighbors(self, node):
        """Return the list of all nodes connected to by edges."""
        return self.graph_dict.get(node)

    def adjacent(self, node1, node2):
        """Return boolean for edges between two nodes."""
        try:
            return node2 in self.graph_dict.get(node1)
        except TypeError:
            return False

    def depth_traversal(self, starting_node):
        if self.has_node(starting_node):
            to_search = [starting_node]
            seen = []
        else:
            raise ValueError('Node does not exist')


    def breadth_traversal(self, starting_node):
        if self.has_node(starting_node):    
            to_search = [starting_node]
            seen = []

            while to_search:
                item = to_search[0]
                children = self.neighbors(item)
                if children:
                    for child in children:
                        if child in seen:
                            continue
                        if child in to_search:
                            continue
                        to_search.append(child)
                to_search.remove(item)
                seen.append(item)

            return seen
        else:
            raise ValueError('Node does not exist')


if __name__ == '__main__':
    obj = SimpleGraph()
    obj.add_node('A')
    obj.add_node('B')
    obj.add_node('C')
    obj.add_node('D')
    obj.add_node('E')
    obj.add_node('F')
    obj.add_node('G')
    obj.add_node('H')
    obj.add_edge('A', 'B')
    obj.add_edge('A', 'C')
    obj.add_edge('A', 'D')
    obj.add_edge('C', 'E')
    obj.add_edge('C', 'F')
    obj.add_edge('D', 'G')
    obj.add_edge('G', 'H')
    obj.breadth_traversal('A')
