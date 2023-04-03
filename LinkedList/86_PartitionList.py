# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        leftHead = ListNode()
        left = ListNode()
        leftHead.next = left
        rightHead = ListNode()
        right = rightHead
        cur = head
        while cur:
            tmp = cur.next
            if cur.val < x:
                cur.next = None
                left.next = cur
                left = left.next
                print(leftHead)
            else:
                cur.next = None
                right.next = cur
                right = right.next
            cur = tmp
        print(leftHead)
        left.next = rightHead.next
        
        return leftHead.next.next