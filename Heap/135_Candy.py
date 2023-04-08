class Solution:
    def candy(self, ratings: List[int]) -> int:
        hp = []
        for i in range(len(ratings)):
            heapq.heappush(hp, (ratings[i], i))
        
        candy = [1] * len(ratings)

        while (hp):
            r, x = heapq.heappop(hp)
            if x > 0 and ratings[x-1] < ratings[x]:
                candy[x] = candy[x-1] + 1
            if x < len(ratings) - 1 and ratings[x+1] < ratings[x]:
                candy[x] = max(candy[x], candy[x+1] + 1)
            # print(f"{r}, {x}")
            # print(candy)
        return sum(candy)