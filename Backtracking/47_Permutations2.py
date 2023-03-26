class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()
        def permute(arr, rem):
            if not rem:
                res.append(arr)
                return
            for i in range(len(rem)):
                if i > 0 and rem[i] == rem[i-1]:
                    continue
                arr.append(rem[i])
                sliced = rem[:i] + rem[i+1:]
                permute(arr[:], sliced[:])
                arr.pop()
        
        permute([], nums)
        return res