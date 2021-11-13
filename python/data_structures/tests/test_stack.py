from data_structures.stack_and_queue.stack_and_queue import Stack
import pytest


def test_push_onto_a_stack(stack):
    expected = "w"
    actual = stack.top.value
    assert expected == actual


def test_push_multiple_values_onto_a_stak():
    expected = "x"
    stack = Stack()
    stack.push("x")
    actual = stack.top.value
    assert expected == actual


def test_pop_off_the_stack(stack):
    expected = "w"
    actual = stack.pop()
    assert expected == actual


def test_pop_empty_a_stack(stack):
    node1 = stack.pop()
    node2 = stack.pop()
    node3 = stack.pop()
    node4 = stack.pop()
    assert stack.is_empty() == True


def test_peek_next_item_on_the_stack(stack):
    expected = "w"
    actual = stack.peek()
    assert expected == actual


def test_instantiate_an_empty_stack():
    stack = Stack()
    assert stack.is_empty() == True


def test_peek_from_empty_stack():
    with pytest.raises(Exception):
        stack = Stack()
        actual = stack.peek()
        expected = "You can't pop an empty stack"
        assert actual == expected


@pytest.fixture
def stack():
    stack = Stack()
    stack.push("x")
    stack.push("y")
    stack.push("z")
    stack.push("w")

    return stack
