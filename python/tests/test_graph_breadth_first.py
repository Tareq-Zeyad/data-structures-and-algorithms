from code_challenges.graph_breadth_first.graph_breadth_first import Graph

import pytest


def test_graphs_breadth_first():
    # Arrange
    graph = Graph()
    first_node = graph.add_node('Pandora')
    second_node = graph.add_node('Arendelle')
    third_node = graph.add_node('Metroville')
    fourth_node = graph.add_node('Monstroplolis')
    fifth_node = graph.add_node('Narnia')
    sixth_node = graph.add_node('Naboo')

    graph.add_edge(first_node, second_node)
    graph.add_edge(second_node, third_node)
    graph.add_edge(second_node, fourth_node)
    graph.add_edge(third_node, fourth_node)
    graph.add_edge(third_node, fifth_node)
    graph.add_edge(third_node, sixth_node)
    graph.add_edge(fourth_node, sixth_node)

    # expected = ['Pandora', 'Arendelle', 'Metroville', 'Monstroplolis', 'Narnia', 'Naboo']
    expected = 6
    # Actual
    actual = graph.size()
    # actual = graph.breadth_first_search(first_node)
    # Assert
    assert actual == expected
