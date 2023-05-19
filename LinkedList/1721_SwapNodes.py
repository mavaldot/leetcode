# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        left = head
        cur = head
        l = k
        while cur:
            cur = cur.next
            l -= 1
            if l == 1: left = cur
            n += 1
        target = n - k
        
        right = head
        while target > 0:
            right = right.next
            target -= 1

        print(left.val)
        print(right.val)

        left.val, right.val = right.val, left.val

        return head