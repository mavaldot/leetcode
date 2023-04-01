class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        currProfit = 0
        minVal = float("inf")
        maxVal = 0
        for i in range(len(prices)):
            if prices[i] > minVal:
                currProfit = prices[i] - minVal
            if prices[i] < minVal:
                minVal = prices[i]
            maxProfit = max(maxProfit, currProfit)
        return maxProfit
