# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None or k == 0: return head
        cur = head
        sz = 0
        last = None
        while cur:
            last = cur
            cur = cur.next
            sz += 1
        k = k % sz
        target = sz - k
        cur = head
        prev = head
        print(sz)
        print(target)
        while target > 0 and cur:
            prev = cur
            cur = cur.next
            target -= 1
        if cur is None: return head
        prev.next = None
        last.next = head

        return cur