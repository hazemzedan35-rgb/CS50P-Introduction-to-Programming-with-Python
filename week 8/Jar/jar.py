class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0 

    def __str__(self):
        result = ""
        for _ in range(self.size):
            result += "🍪"
        return result

    def deposit(self, n):
        if (self.size + n) > self.capacity:
            raise ValueError()
        self.size += n

    def withdraw(self, n):
        if self.size < n:
            raise ValueError()
        self.size -= n 

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("capacity cannot be a negative number.")
        elif isinstance(capacity, float) and not capacity.is_integer():
            raise ValueError("capacity cannot be a decimal number.")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size < 0:
            raise ValueError()
        elif isinstance(size, float) and not size.is_integer():
            raise ValueError()
        self._size = size


