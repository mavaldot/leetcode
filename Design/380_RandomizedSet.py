class RandomizedSet:

    def __init__(self):
        self.randomSet = set()

    def insert(self, val: int) -> bool:
        if val in self.randomSet: return False
        self.randomSet.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.randomSet:
            self.randomSet.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        l = list(self.randomSet)
        return l[random.randint(0, len(l)-1)]