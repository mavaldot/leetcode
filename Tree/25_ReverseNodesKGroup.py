class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        curr = dummy
        
        while curr:
            group = []
            i = 0
            prev = curr
            curr = curr.next
            
            while (i < k):
                
                if curr is None: break
                group.append(curr)
                i += 1
                curr = curr.next
            
            if i < k: break

            group_head = group.pop()
            prev.next = group_head
            nxt = group_head.next

            while group:
                group_head.next = group.pop()
                group_head = group_head.next

            group_head.next = nxt
            curr = group_head
        
        return dummy.next