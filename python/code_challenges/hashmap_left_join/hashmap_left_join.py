
def left_join(table_one: dict, table_two: dict):
    """A function that joins the second provided dictionary to the first dictionary(aka hashtables)
     and returns a list.
    Args:
        table_one (dict): hashmap to be merged to
        table_two (dict): hashap to be merged
    Returns:
        [type]: list of lists containing key and values of the provided hashmaps.
    """
    list_of_items = []
    for key, val in table_one.items():
        val2 = table_two.get(key)
        list_of_items.append([key, val, val2])

    return list_of_items
