class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        helper = ListNode()
        helper.next = head
        left = helper
        cur = head

        while cur:
            nxt = cur.next
            if nxt is None:
                break
            tmp = nxt.next
            left.next = nxt
            nxt.next = cur
            cur.next = tmp
            left = cur
            cur = tmp
        
        return helper.next