class DynamicArray:
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be > 0")
        self._capacity = capacity           # total capacity
        self._size = 0                      # current number of elements
        self._data = [None] * capacity      # underlying fixed-size storage

    def get(self, i: int) -> int:
        # assume i is valid: 0 <= i < self._size
        return self._data[i]

    def set(self, i: int, n: int) -> None:
        # assume i is valid: 0 <= i < self._size
        self._data[i] = n

    def pushback(self, n: int) -> None:
        # if array is full, resize first
        if self._size == self._capacity:
            self.resize()
        self._data[self._size] = n
        self._size += 1

    def popback(self) -> int:
        # assume array is non-empty: self._size > 0
        value = self._data[self._size - 1]
        # (optional) clear the slot
        self._data[self._size - 1] = None
        self._size -= 1
        return value

    def resize(self) -> None:
        # double the capacity
        new_capacity = self._capacity * 2
        new_data = [None] * new_capacity
        # copy existing elements
        for i in range(self._size):
            new_data[i] = self._data[i]
        # switch to new storage
        self._data = new_data
        self._capacity = new_capacity

    def getSize(self) -> int:
        return self._size

    def getCapacity(self) -> int:
        return self._capacity
