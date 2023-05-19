class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        maxTwinSum = 0
        
        cur = head
        while cur:
            arr.append(cur.val)
            cur = cur.next

        mid = len(arr) // 2
        for i in range(mid):
            twinSum = arr[i] + arr[~i]
            maxTwinSum = max(maxTwinSum, twinSum)
        
        return maxTwinSum