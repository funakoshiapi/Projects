"""
Funakoshi Silva
"""


class HashNode:
    """
    DO NOT EDIT
    """
    __slots__ = ["key", "value", "deleted"]

    def __init__(self, key, value, deleted=False):
        self.key = key
        self.value = value
        self.deleted = deleted

    def __repr__(self):
        return f"HashNode({self.key}, {self.value})"

    def __eq__(self, other):
        return self.key == other.key and self.value == other.value

    def __iadd__(self, other):
        self.value += other


class HashTable:
    """
    Hash Table Class
    """
    __slots__ = ['capacity', 'size', 'table', 'prime_index']

    primes = (
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
        89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179,
        181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277,
        281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389,
        397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499,
        503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617,
        619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739,
        743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859,
        863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991,
        997)

    def __init__(self, capacity=8):
        """
        DO NOT EDIT
        Initializes hash table
        :param capacity: capacity of the hash table
        """
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

        i = 0
        while HashTable.primes[i] <= self.capacity:
            i += 1
        self.prime_index = i - 1

    def __eq__(self, other):
        """
        DO NOT EDIT
        Equality operator
        :param other: other hash table we are comparing with this one
        :return: bool if equal or not
        """
        if self.capacity != other.capacity or self.size != other.size:
            return False
        for i in range(self.capacity):
            if self.table[i] != other.table[i]:
                return False
        return True

    def __repr__(self):
        """
        DO NOT EDIT
        Represents the table as a string
        :return: string representation of the hash table
        """
        represent = ""
        bin_no = 0
        for item in self.table:
            represent += "[" + str(bin_no) + "]: " + str(item) + '\n'
            bin_no += 1
        return represent

    def _hash_1(self, key):
        """
        ---DO NOT EDIT---
        Converts a string x into a bin number for our hash table
        :param key: key to be hash_operation
        :return: bin number to insert hash item at in our table, None if key is an empty string
        """
        if not key:
            return None
        hashed_value = 0

        for char in key:
            hashed_value = 181 * hashed_value + ord(char)
        return hashed_value % self.capacity

    def _hash_2(self, key):
        """
        ---DO NOT EDIT---
        Converts a string x into a hash
        :param x: key to be hash_operation
        :return: a hash_operation value
        """
        if not key:
            return None
        hashed_value = 0

        for char in key:
            hashed_value = 181 * hashed_value + ord(char)

        prime = HashTable.primes[self.prime_index]

        hashed_value = prime - (hashed_value % prime)
        if hashed_value % 2 == 0:
            hashed_value += 1
        return hashed_value

    def __len__(self):
        """
        don't edit this plz
        Getter for size
        :return: size
        """
        return self.size

    ########## EDIT BELOW ##########

    def __setitem__(self, key, value):
        """
        Creates a node in the hash table that has the
        key and value that are passed in as parameters
        :param key: used for item
        :param value: used for item
        :return None
        """
        self._insert(key, value)

    def __getitem__(self, key):
        """
        Gets the item with the key denoted by the item parameter
        :param key: used for item
        :return item.value
        """
        item = self._get(key)

        if item is None:
            raise KeyError(' incorrect key' + key)
        else:
            return item.value

    def __delitem__(self, key):
        """
         Deletes the node that has the value denoted by the
        :param key: used for item
        :return: type None
        """
        self._delete(key)

    def __contains__(self, key):
        """
        Determines if a node with the key denoted
        by the item parameter exists in the table
        :param key
        :return bool
        """

        for node in self.table:
            if node and node.key is not key:
                return False
            if node and node.key == key:
                return True

    def hash(self, key, inserting=False):
        """
        Given a key string return 
        an index in the hash table
        Uses double hashing
        param: key: item key
        param: inserting: boolean value
        return: type int
        """

        index = 0
        has_2 = index * self._hash_2(key)
        has_1 = self._hash_1(key)
        hash_operation = (has_1 + has_2) % self.capacity

        while True:

            if inserting is True:
                if self.table[hash_operation] is None:
                    return hash_operation

                if self.table[hash_operation].deleted is True:
                    return hash_operation
                else:
                    if not self.table[hash_operation].key:
                        return hash_operation
                    else:
                        if self.table[hash_operation].key == key:
                            return hash_operation
            else:
                if inserting is False:
                    if self.table[hash_operation] is None:
                        return hash_operation

                    else:
                        if self.table[hash_operation].key == key:
                            return hash_operation
            index += 1
            has_2 = index * self._hash_2(key)
            has_1 = self._hash_1(key)
            hash_operation = (has_1 + has_2) % self.capacity

    def _insert(self, key, value):
        """
        Use the key and value parameters to
         add a HashNode to the hash table.
         :param key
         :param value
         :return none
        """
        index = self.hash(key, True)

        # mambo mudamanbo

        if self.table[index] is None:
            self.size += 1
        else:
            if self.table[index].deleted:
                self.size += 1

        factor_growth = self.capacity // 2

        self.table[index] = HashNode(key, value)

        if factor_growth <= self.size:
            self._grow()

    def _get(self, key):
        """
        Find the HashNode with the given key in the hash table.
        :return type Node
        """
        if self.table[self.hash(key, False)]:

            return self.table[self.hash(key, False)]
        else:
            return None

    def _delete(self, key):
        """
        Removes the HashNode with the given
        key from the hash table .
        :param key
        :return type None
        """
        index = self.hash(key, False)

        self.table[index].key = None
        self.table[index].value = None
        self.table[index].deleted = True
        self.size -= 1

        if self.table[index] is None:
            raise KeyError('incorrect key: ' + key)

    def _grow(self):
        """
         Double the capacity of the existing hash table.
        :return type None
        """
        index = 0
        self.size = 0

        current = list(self.items())

        self.capacity *= 2

        self.table = self.capacity * [None]

        while True:
            if HashTable.primes[index] <= self.capacity:
                index += 1
            else:
                break

        self.prime_index = index - 1

        for key_g, value_g in current:
            self[key_g] = value_g

    def update(self, pairs=[]):
        """
        Double the capacity of the existing hash table.
        :return type None
       """
        for key_g, value_g in pairs:
            self._insert(key_g, value_g)

    def setdefault(self, key, default=None):
        """
        Sets the default value for the key denoted
        by the key parameter using the default parameter
        :param key
        :param default
        :return
        """
        # test this
        if key not in self:
            self._insert(key, default)
            return default
        else:
            return self._get(key).value

    def keys(self):
        """
        Returns a generator object that contains
        all of the keys in the table
        :return: type generator
        """
        for my_key in self.table:
            if my_key:
                yield my_key.key

    def values(self):
        """
        Returns a generator object that contains
        all of the values in the table
        :return: type generator
        """
        for my_value in self.table:
            if my_value:
                yield my_value.value

    def items(self):
        """
        Returns a generator object that contains
        all of the items in the table
        :return: type generator
        """
        for item in self.table:
            if item:
                yield item.key, item.value

    def clear(self):
        """
        Completely clears table of hash Nodes
        :return: type None
        """

        index = 0
        limit = range(self.capacity)

        while index in limit:
            if self.table[index]:
                self.table[index] = None
                self.size -= 1
            index += 1


def hurdles(grid):
    """
     determine the minimum number of hurdles you will
     need to jump over to win the race.
     :param grid: reference to the grid size
     :return int: number of hurdles
    """
    table = HashTable()
    grid_size = len(grid)

    #index = 0
    #index3 = 0

    for line in grid:
        value = line[0]
        index = 0
        # index += 1
        last_border = len(line) - 1
        while True:

            if value not in table:
                table[str(value)] = 1
            else:
                table[str(value)] = table[str(value)] + 1

            if index < last_border:
                value = value + line[index + 1]
                index = index + 1
            else:
                break

        # can't figure it out what to do here
        # table.items()  need second biggest value of the tuple
        obstacle = 0
        best_path = grid_size - obstacle


    return best_path
