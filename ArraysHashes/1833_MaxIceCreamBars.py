class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        bars = 0
        for cost in costs:
            coins -= cost
            if coins < 0:
                return bars
            bars += 1
        return bars