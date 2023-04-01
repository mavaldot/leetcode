class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums = sorted(nums)
        print(nums)
        ans = []

        for item in queries:
            i = 0
            nums_sum = 0
            for x in range(0, len(nums)):
                nums_sum += nums[x]
                if (nums_sum > item):
                    break
                else:
                    i += 1
            ans.append(i)
        return ans