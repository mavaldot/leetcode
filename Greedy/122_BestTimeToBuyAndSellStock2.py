class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = -prices[0]
        lastBuy = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < lastBuy:
                profit += lastBuy
                lastBuy = prices[i]
                profit -= prices[i]
            elif prices[i] > lastBuy:
                lastBuy = prices[i]

        profit += lastBuy
        return profit