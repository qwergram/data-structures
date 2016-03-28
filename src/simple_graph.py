# -*- coding: utf-8 -*-
"""Simple Graph structure."""
import collections
from itertools  import count
from heapq import heappop, heappush


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
        self.graph_dict.setdefault(node, {})

    def add_edge(self, node1, node2, weight=1):
        """Add a edge from node 1 to node 2."""
        self.add_node(node1)
        self.add_node(node2)
        self.graph_dict[node1][node2] = weight

    def del_node(self, node):
        """Delete the node from the graph."""
        try:
            del self.graph_dict[node]
            for key in self.graph_dict:
                if node in self.graph_dict[key]:
                    del self.graph_dict[key][node]
        except KeyError:
            raise KeyError('Node does not exist')

    def del_edge(self, node1, node2):
        """Delete the edge connecting node 1 and node 2."""
        try:
            self.graph_dict[node1]
        except KeyError:
            raise KeyError('Node1 does not exist')
        try:
            del self.graph_dict[node1][node2]
        except KeyError:
            raise ValueError('Node2 does not exist')

    def has_node(self, node):
        """Return a boolean for if node exists."""
        return isinstance(self.graph_dict.get(node), dict)

    def neighbors(self, node):
        """Return the list of all nodes connected to by edges."""
        try:
            return set(self.graph_dict.get(node).keys())
        except AttributeError:
            return None

    def adjacent(self, node1, node2):
        """Return boolean for edges between two nodes."""
        try:
            return node2 in self.graph_dict.get(node1)
        except TypeError:
            return False

    def depth_traversal(self, starting_node):
        """Traverse the graph in a traverse modality."""
        if self.has_node(starting_node):
            to_search = [starting_node]
            seen = []
            while to_search:
                item = to_search[0]
                children = self.neighbors(item)
                if children:
                    for index, child in enumerate(children):
                        if child in seen:
                            continue
                        if child in to_search:
                            continue
                        to_search.insert(index + 1, child)
                to_search.remove(item)
                seen.append(item)
            seen = set(seen)

        else:
            raise ValueError('Node does not exist')
        return seen

    def breadth_traversal(self, starting_node):
        """Traverse the graph in a breadth modality."""
        if self.has_node(starting_node):
            to_search = collections.deque(starting_node)
            seen = set()
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
                item = to_search.popleft()
                seen.update(item)

            return seen
        else:
            raise ValueError('Node does not exist')

    def shortest_path_dijkstra(self, node1, node2):
        unique = 1
        visited = set()
        heap = [(0, unique, node1, (None,))]
        while heap:
            cumulative, unique, node, path = heappop(heap)
            if node not in visited:
                visited.add(node)
                if node2 == node:
                    path = (node2, path)
                    pretty_path = []
                    while True:
                        try:
                            current, path = path
                            pretty_path.append(current)
                    # return path, cumulative
                        except ValueError:
                            return pretty_path[::-1]
                for neighbor, edge_weight in self.graph_dict[node].items():
                    unique += 1
                    heappush(heap, (cumulative + edge_weight, unique, neighbor, (node, path)))


    def floyd_path(self):
        dist = {}
        for node in self.graph_dict:
            dist[node] = {}
            dist[node][node] = 0
        for node1 in dist:
            for node2 in dist:
                try:
                    dist[node1][node2] = self.graph_dict[node1][node2]
                except KeyError:
                    pass
        for k in self.graph_dict:
            for i in self.graph_dict:
                for j in self.graph_dict:
                    try:
                        if dist[i][j] > dist[i][k] + dist[k][j]:
                            dist[i][j] = dist[i][k] + dist[k][j]
                    except KeyError:
                        pass
        import pdb; pdb.set_trace()



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
    obj.add_edge('A', 'B', 45000000)
    obj.add_edge('A', 'C', .5)
    obj.add_edge('A', 'D', 8)
    obj.add_edge('C', 'E', 0)
    obj.add_edge('C', 'F', 1)
    obj.add_edge('D', 'G', 7)
    obj.add_edge('G', 'H')
    obj.floyd_path()
