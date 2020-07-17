class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.current = 0

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)

        self.storage[self.current] = item

        self.current += 1

        if self.current > self.capacity -1:
            self.current = 0

    def get(self):
        return self.storage 