from data_structures.hash_tables.hash_tables import HashTable
import pytest


@pytest.fixture
def hashtable():
    return HashTable()


def test_hash(hashtable: HashTable):
    expected = 700
    actual = hashtable._HashTable__hash("d")
    assert actual == expected


def test_hash_word(hashtable: HashTable):
    expected = 376
    actual = hashtable._HashTable__hash("dd")
    assert actual == expected


def test_add(hashtable: HashTable):
    # Arrange
    expected = True
    hashtable.add("car_color", "red")
    # Actual
    actual = hashtable.contains("car_color")
    # Assert
    assert actual == expected


def test_get_value(hashtable: HashTable):
    # Arrange
    expected = "red"
    hashtable.add("car_color", "red")
    # Actual
    actual = hashtable.get("car_color")
    # Assert
    assert actual == expected


def test_doesnt_exist(hashtable: HashTable):
    # Arrange
    expected = None
    # Actual
    actual = hashtable.get("car_color")
    # Assert
    assert actual == expected


def test_get_value(hashtable: HashTable):
    # Arrange
    expected = "red"
    hashtable.add("car_color", "red")
    # Actual
    actual = hashtable.get("car_color")
    # Assert
    assert actual == expected


def test_retrive_val_collision(hashtable: HashTable):
    # Arrange
    expected = "red"
    first_val = "ad"  # hash = 355
    second_val = "da"  # hash = 355

    hashtable.add(first_val, "red")
    hashtable.add(second_val, "black")
    # Actual
    actual = hashtable.get(first_val)
    # Assert
    assert actual == expected

# Successfully hash a key to an in-range value


def test_hash_in_range(hashtable: HashTable):
    # Arrange
    expected = 465
    # Actual
    actual = hashtable._HashTable__hash("pc_part_color")
    # Assert
    assert actual == expected
