# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = head
        avoid = inf
        prev = dummy
        while cur:
            if cur.val == avoid:
                cur = cur.next
                continue
            elif cur.next and cur.next.val == cur.val:
                avoid = cur.val
            else:
                prev.next = cur
                prev = cur
            cur = cur.next
            prev.next = None
        return dummy.next