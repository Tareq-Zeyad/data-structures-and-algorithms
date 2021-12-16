from attr import has
from code_challenges.hashmap_left_join.hashmap_left_join import left_join
import pytest


@pytest.fixture
def hashtable_one():
    hashtable = {}
    hashtable['fond'] = 'enamored'
    hashtable['wrath'] = 'anger'
    hashtable['diligent'] = 'employed'
    hashtable['outfit'] = 'garb'
    hashtable['guide'] = 'usher'
    return hashtable


@pytest.fixture
def hashtable_two():
    hashtable = {}
    hashtable['fond'] = 'averse'
    hashtable['wrath'] = 'delight'
    hashtable['diligent'] = 'idle'
    hashtable['guide'] = 'follow'
    hashtable['flow'] = 'jam'
    return hashtable


@pytest.fixture
def empty_hashtable():
    hashtable = {}
    return hashtable


@pytest.fixture
def empty_hashtable_two():
    hashtable = {}
    return hashtable


def test_hashmap_left_join(hashtable_one, hashtable_two):
    # Arrange
    expected = [
        ['fond', 'enamored', 'averse'],
        ['wrath', 'anger', 'delight'],
        ['diligent', 'employed', 'idle'],
        ['outfit', 'garb', None],
        ['guide', 'usher', 'follow']
    ]
    # Actual
    actual = left_join(hashtable_one, hashtable_two)

    # Assert
    assert actual == expected


def test_hashmap_left_join_two(empty_hashtable, empty_hashtable_two):
    # Arrange
    expected = []
    # Actual
    actual = left_join(empty_hashtable, empty_hashtable_two)
    # Assert
    assert actual == expected
