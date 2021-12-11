# Hashtables

- Hash table (hash map) is a data structure that implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index, also called a hash code, into an array of buckets or slots, from which the desired value can be found.

## Challenge

- To Implement a Hashtable Class with the following methods:

* add

* get

* contains

* hash


## Approach & Efficiency

- Approach: Whiteboarding > Coding > Testing.

- Efficiency:

**for add and hash**:

* Time = O(1)
* Space = O(1)

**for contains and retrive**:

* Time = O(n)
* Space = O(1)

## API

```
* HashTable Class:
    Arguments: Optional (_Size defaults to 1024)

* add method:
    Arguments: key, value
    Returns: nothing
    This method should hash the key, and add the key and value pair to the table, handling collisions as needed.
* get method:
    Arguments: key
    Returns: Value associated with that key in the table
* contains method:
    Arguments: key
    Returns: Boolean, indicating if the key exists in the table already.
* hash method:
    Arguments: key
    Returns: Index in the collection for that key
```