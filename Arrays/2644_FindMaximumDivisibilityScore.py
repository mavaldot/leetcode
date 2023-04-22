class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        divs = set()
        maxScore = -1
        maxDiv = inf
        for i in range(len(divisors)):
            score = 0
            if divisors[i] in divs: continue
            for j in range(len(nums)):
                if nums[j] % divisors[i] == 0:
                    score += 1
            if score > maxScore:
                maxScore = score
                maxDiv = divisors[i]
            elif score == maxScore:
                maxDiv = min(maxDiv, divisors[i])
            divs.add(divisors[i])
        
        return maxDiv