class CircularBuffer(list):
    def __getitem__(self, key):
        return super(CircularBuffer, self).__getitem__(key % len(self))
