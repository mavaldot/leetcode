from bisect import bisect_left


class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        prefixSum = [0] * n
        sm = 0
        for i in range(n):
            sm += nums[i]
            prefixSum[i] = sm
        
        res = []
        for query in queries:
            idx = bisect_left(nums, query)
            ops = 0
            if idx > 0:
                print(idx)
                right = prefixSum[n-1] - prefixSum[idx-1] - query * (n-idx)
                left = abs(prefixSum[idx-1] - query * (idx))
                print(f"{left}, {right}")
                ops = left + right
            else:
                ops += prefixSum[n-1] - n*query
            res.append(ops)

        return res