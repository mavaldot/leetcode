from sortedcontainers import SortedList

class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        ls = SortedList()
        res = []
        for i in range(k-1):
            ls.add(nums[i])

        
        for i in range(k-1, len(nums)):
            ls.add(nums[i])
            if ls[x-1] < 0:
                res.append(ls[x-1])
            else:
                res.append(0)
            ls.remove(nums[i-k+1])
            
        return res