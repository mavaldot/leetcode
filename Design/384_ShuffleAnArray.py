class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = nums[:]

    def reset(self) -> List[int]:
        self.nums = self.original[:]
        return self.nums

    def shuffle(self) -> List[int]:
        for i in range(len(self.nums)):
            j = random.randint(0, len(self.nums)-1)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums