class PrefixMapSum:
    '''
    This problem was asked by Google.

    Implement a PrefixMapSum class with the following methods:

    insert(key: str, value: int): Set a given key's value in the map.
    If the key already exists, overwrite the value.
    sum(prefix: str): Return the sum of all values of keys that begin with a
    given prefix.
    For example, you should be able to run the following code:

    mapsum.insert("columnar", 3)
    assert mapsum.sum("col") == 3

    mapsum.insert("column", 2)
    assert mapsum.sum("col") == 5
    '''

    def __init__(self):
        self.__the_map = dict()

    def insert(self, key, value):
        self.__the_map[key] = value

    def sum(self, prefix):
        return sum([v for k, v in self.__the_map.items() if
                    str(k).startswith(prefix)])


if __name__ == "__main__":
    prefix_map = PrefixMapSum()
    prefix_map.insert('columnar', 3)
    assert prefix_map.sum('col') == 3

    prefix_map.insert('column', 2)
    assert prefix_map.sum('col') == 5
