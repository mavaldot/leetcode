class SmallestInfiniteSet:

    def __init__(self):
        self.smallest = 1
        self.heap = []
        self.st = set()

    def popSmallest(self) -> int:
        if len(self.heap) < 1 or self.heap[0] > self.smallest:
            self.smallest += 1
            return self.smallest - 1
        else:
            num = heapq.heappop(self.heap)
            self.st.remove(num)
            return num
            

    def addBack(self, num: int) -> None:
        if num < self.smallest:
            if num not in self.st:
                self.st.add(num)
                heapq.heappush(self.heap, num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)