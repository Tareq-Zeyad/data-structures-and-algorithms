# from data_structures.stack_and_queue.stack_and_queue import Queue
# import pytest


# def test_is_empty():
#     """
#     Testing wether the queue empty or not, boolean values
#     """
#     queue = Queue()
#     expected = True
#     actual = queue.is_empty()
#     assert expected == actual


# def test_enqueue():
#     """
#     Testing for adding items in the rear/back of a queue.
#     """
#     queue = Queue()
#     queue.enqueue("a")
#     expected = "a"
#     actual = queue.rear.value
#     assert expected == actual


# def test_multiple_enqueues_into_queue(queue):
#     expected = "w"
#     actual = queue.rear.value
#     assert expected == actual


# def test_dequeue_from_queue(queue):
#     expected = "x"
#     actual = queue.dequeue()
#     assert expected == actual


# def test_peek_from_queue(queue):
#     expected = "x"
#     actual = queue.peek()
#     assert expected == actual


# def test_peek_from_queue_after_multiple_dequeues(queue):
#     node1 = queue.dequeue()
#     node2 = queue.dequeue()
#     node3 = queue.dequeue()
#     node4 = queue.dequeue()
#     assert queue.is_empty() == True


# def test_instantiate_an_empty_queue():
#     queue = Queue()
#     assert queue.front == None


# def test_peek_from_empty_queue():
#     with pytest.raises(Exception):
#         queue = Queue()
#         actual = queue.peek()
#         expected = "an empty Queue"
#         assert actual == expected


# @pytest.fixture
# def queue():
#     queue = Queue()
#     queue.enqueue("x")
#     queue.enqueue("y")
#     queue.enqueue("z")
#     queue.enqueue("w")

#     return queue
