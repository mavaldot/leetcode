class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        self.res = []

        def search(i, curSum, arr):
            if i < 0 or curSum > target:
                return
            print(f"i: {i}")
            while (curSum < target):
                search(i-1, curSum, arr[:])
                print(curSum)
                curSum += candidates[i]
                arr.append(candidates[i])
                if curSum == target:
                    self.res.append(arr)
                    break
                
        
        search(len(candidates) - 1, 0, [])

        return self.res