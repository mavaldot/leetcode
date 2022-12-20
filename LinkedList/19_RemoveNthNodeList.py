class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if not head or not head.next:
            return None
        
        slow = fast = head
        i = 0
        sz = 1
        while fast and fast.next:
            i+=1
            sz+=2
            slow = slow.next
            fast = fast.next.next
            if fast is None: sz -= 1
        
        target = sz - n - 1
        
        if (target < 0):
            return head.next

        counter = 0

        if (target < i):
            slow = head
        else:
            counter += i

        while (counter < target):
            slow = slow.next
            counter += 1

        if slow.next:
            next_node = slow.next.next
            slow.next = next_node
        else:
            slow.next = None

        print(slow.val)

        print(f"slow: {i}")
        print(f"size: {sz}")

        return head