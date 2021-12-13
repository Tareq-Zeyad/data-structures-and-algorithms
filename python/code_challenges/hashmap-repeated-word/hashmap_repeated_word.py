from data_structures.hash_tables.hash_tables import HashTable
import string


def repeated_word(_string: str):
    """A function that returns the most repeated word in a string.
    Args:
        string (str): string to be scanned.
    Returns:
        [type]: the most repeated word in the provided string.
    """
    hash_table = HashTable()
    most_repeated_word = ""
    list_of_words = _string.split(" ")

    for i in list_of_words:
        i = i.translate(str.maketrans('', '', string.punctuation))
        if hash_table.contains(i):
            most_repeated_word = i
            break
        else:
            if not i.strip("-").isnumeric():
                hash_table.add(i.lower(), 5)

    return most_repeated_word
