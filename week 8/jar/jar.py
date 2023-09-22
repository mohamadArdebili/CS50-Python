
class Jar:
    def __init__(self, capacity=12):
        if capacity >= 0:
            self._capacity = capacity
        else:
            raise ValueError
        self.cookie = 0

    def __str__(self):
        return self.cookie * "🍪"

    def deposit(self, n):
        self.cookie = self.cookie + n
        if self.cookie > self.capacity:
            raise ValueError

    def withdraw(self, n):
        if n <= self.cookie:
            self.cookie = self.cookie - n
        else:
            raise ValueError
    # getter
    @property
    def capacity(self):
        # don't want to update the variable.
        return self._capacity

    # setter
    @property
    def size(self):
        return self.cookie

def main():
    print(Jar())

if __name__ == "__main__":
    main()
