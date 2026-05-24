import random

class RandomizedSet:

    def __init__(self):
        self.exists = dict()

    def insert(self, val: int) -> bool:
        if val in self.exists:
            return False
        self.exists[val] = True
        return True

    def remove(self, val: int) -> bool:
        if val in self.exists:
            self.exists[val] = False
            return True
        return False

    def getRandom(self) -> int:
        i = random.randint(0, len(self.exists.keys()) - 1)
        return list(self.exists.keys())[i]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()