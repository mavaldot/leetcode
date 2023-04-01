class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        m1 = min(nums1)
        m2 = min(nums2)
        
        com = 10
        
        for i in range(1, 10):
            if i in nums1 and i in nums2:
                com = i
                break
        
        
        
        if com < 10: return com
        return min(m1,m2) * 10 + max(m1,m2)