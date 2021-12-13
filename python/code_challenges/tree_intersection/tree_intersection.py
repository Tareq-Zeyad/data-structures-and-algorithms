from data_structures.trees.trees import BinaryTree
from data_structures.hash_tables.hash_tables import HashTable


def tree_intersection(first_tree: BinaryTree, second_tree: BinaryTree):
    first_tree_items = first_tree.pre_order()
    second_tree_items = second_tree.pre_order()
    list_of_matched_items = []
    hashtable = HashTable()

    for i, val in enumerate(first_tree_items):
        val = f"{val}"
        item = hashtable.get(val)
        if not item:
            hashtable.add(val, 1)

    for i, val in enumerate(second_tree_items):
        val = f"{val}"
        item = hashtable.get(val)
        if item:
            list_of_matched_items.append(val)

    return list_of_matched_items
