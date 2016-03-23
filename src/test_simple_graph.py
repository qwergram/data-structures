# -*- coding: utf-8 -*-
import pytest

@pytest.fixture(scope='function')
def fixture_graph():
    """Create a fixture."""
    from simple_graph import SimpleGraph
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
    return obj


def test_breadth(fixture_graph):
    """Test that to_search is the correct outcome path."""
    test = fixture_graph.breadth_traversal('A')
    assert test == ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']


def test_breadth_small(fixture_graph):
    """Test that to_search is the correct outcome path."""
    test2 = fixture_graph.breadth_traversal('G')
    assert test2 == ['G', 'H']


def test_nonexistant_node_breadth(fixture_graph):
    """Test breath function on a non-existant node."""
    with pytest.raises(ValueError):
        fixture_graph.breadth_traversal('I')


def test_depth(fixture_graph):
    """Test that to_search is the correct outcome path."""
    test = fixture_graph.depth_traversal('A')
    assert test == ['A', 'B', 'C', 'E', 'F', 'D', 'G', 'H']


def test_depth_small(fixture_graph):
    """Test that to_search is the correct outcome path."""
    test2 = fixture_graph.depth_traversal('G')
    assert test2 == ['G', 'H']


def test_nonexistant_node_depth(fixture_graph):
    """Test breath function on a non-existant node."""
    with pytest.raises(ValueError):
        fixture_graph.depth_traversal('I')


def test_add_node():
    """Test add node."""
    from simple_graph import SimpleGraph
    instance = SimpleGraph()
    instance.add_node("waffles")
    instance.add_node("waffles2")
    instance.add_node("waffles3")
    assert 'waffles' in instance.graph_dict
    assert 'waffles2' in instance.graph_dict
    assert 'waffles3' in instance.graph_dict


def test_display_nodes():
    from simple_graph import SimpleGraph
    instance = SimpleGraph()
    instance.add_node("waffles")
    instance.add_node("waffles2")
    instance.add_node("waffles3")
    for waffle in ['waffles', 'waffles2', 'waffles3']:
        assert waffle in instance.nodes()


def test_add_edge():
    from simple_graph import SimpleGraph
    instance = SimpleGraph()
    instance.add_node("waffles")
    instance.add_node("waffles2")
    instance.add_edge('waffles', 'waffles2')
    assert 'waffles2' in instance.graph_dict['waffles']


def test_add_edge_not_exist():
    from simple_graph import SimpleGraph
    instance = SimpleGraph()
    instance.add_edge('waffles', 'waffles2')
    assert 'waffles2' in instance.graph_dict['waffles']


def test_edge_display():
    from simple_graph import SimpleGraph
    instance = SimpleGraph()
    instance.add_edge('waffles', 'waffles2')
    assert instance.edges()[0] == 'waffles-waffles2'


def test_edge_display_empty():
    from simple_graph import SimpleGraph
    instance = SimpleGraph()
    assert instance.edges() == []


def test_del_node():
    from simple_graph import SimpleGraph
    instance = SimpleGraph()
    instance.add_node("waffles")
    instance.del_node('waffles')
    assert instance.graph_dict == {}


def test_del_node_edge():
    from simple_graph import SimpleGraph
    instance = SimpleGraph()
    instance.add_edge('waffles', 'waffles2')
    instance.del_node('waffles2')
    assert instance.graph_dict == {'waffles': {}}


def test_del_edge():
    from simple_graph import SimpleGraph
    instance = SimpleGraph()
    instance.add_edge('waffles', 'waffles2')
    instance.add_edge('waffles', 'waffles3')
    instance.del_edge('waffles', 'waffles2')
    assert instance.graph_dict['waffles'] == {'waffles3': 1}


def test_del_non_existent_node1():
    from simple_graph import SimpleGraph
    instance = SimpleGraph()
    with pytest.raises(KeyError):
        instance.del_edge('waffles', 'waffles2')


def test_del_non_existent_node2():
    from simple_graph import SimpleGraph
    instance = SimpleGraph()
    instance.add_node("waffles")
    with pytest.raises(ValueError):
        instance.del_edge('waffles', 'waffles2')


def test_has_node():
    from simple_graph import SimpleGraph
    instance = SimpleGraph()
    instance.add_node("waffles")
    assert instance.has_node("waffles")


def test_has_node_doesnt_exist():
    from simple_graph import SimpleGraph
    instance = SimpleGraph()
    assert instance.has_node("waffles") is False


def test_neighbors():
    from simple_graph import SimpleGraph
    instance = SimpleGraph()
    instance.add_edge('waffles', 'waffles2')
    instance.add_edge('waffles', 'waffles3')
    assert instance.neighbors('waffles') == {'waffles2', 'waffles3'}


def test_neighbors_empty():
    from simple_graph import SimpleGraph
    instance = SimpleGraph()
    assert instance.neighbors('waffles') is None


def test_adjacent():
    from simple_graph import SimpleGraph
    instance = SimpleGraph()
    instance.add_edge('waffles', 'waffles2')
    assert instance.adjacent('waffles', 'waffles2')


def test_adjacent_empty():
    from simple_graph import SimpleGraph
    instance = SimpleGraph()
    assert instance.adjacent('waffles', 'waffles2') is False
