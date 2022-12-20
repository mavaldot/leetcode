class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None: return None
        prev = head
        curr = head.next
        head.next = None
        while (True):
            if curr is None: return prev
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt