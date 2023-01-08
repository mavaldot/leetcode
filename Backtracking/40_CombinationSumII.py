class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        comb = []
        
        def search(i, arr, sum):
            if sum == target:
                comb.append(arr[:])
                return
            if i >= len(candidates) or sum > target:
                return
            arr.append(candidates[i])
            sum += candidates[i]
            search(i + 1, arr, sum)
            arr.pop()
            j = i
            while (j + 1 < len(candidates)):
                if candidates[j] == candidates[j+1]:
                    j += 1
                else:
                    break
            search(j + 1, arr, sum - candidates[i])
        
        search(0, [], 0)

        return comb