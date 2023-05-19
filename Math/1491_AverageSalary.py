class Solution:
    def average(self, salary: List[int]) -> float:
        minItem = inf
        maxItem = -inf
        total = 0
        for item in salary:
            minItem = min(minItem, item)
            maxItem = max(maxItem, item)
            total += item
        res = (total - minItem - maxItem) / (len(salary) - 2)
        return res