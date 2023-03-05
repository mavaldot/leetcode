class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        prevVal = float("-inf")
        curr = head

        while curr is not None:
            if curr.val != prevVal:
                prevVal = curr.val
                temp = curr.next
                prev = curr
                curr = temp
            else:
                prev.next = curr.next
                curr = curr.next

        return head