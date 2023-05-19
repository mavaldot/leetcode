class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        st = set(int(x, 2) for x in nums)
        
        for i in range(2**n):
            if i not in st:
                return f"{i:>0{n}b}"