# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oddHead = ListNode()
        oddTail = oddHead
        evenHead = ListNode()
        evenTail = evenHead

        cnt = 1

        cur = head
        while cur:
            if cnt & 1:
                oddTail.next = cur
                oddTail = cur
            else:
                evenTail.next = cur
                evenTail = cur
            cur = cur.next
            cnt += 1
        
        oddTail.next = evenHead.next
        evenTail.next = None
        return oddHead.next