class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums2:
            return
        i = m - 1
        j = n - 1
        idx = len(nums1) - 1
        while (i >= 0 and j >= 0):
            if nums1[i] >= nums2[j]:
                nums1[idx] = nums1[i]
                i -= 1
            else:
                nums1[idx] = nums2[j]
                j -= 1
            idx -= 1

        while (idx >= 0 and i >= 0):
            nums1[idx] = nums1[i]
            i -= 1
            idx -= 1
        while (idx >= 0 and j >= 0):
            nums1[idx] = nums2[j]
            j -= 1
            idx -= 1 