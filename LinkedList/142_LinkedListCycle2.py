class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visit = set()

        cur = head
        while (cur):
            if cur in visit:
                return cur
            visit.add(cur)
            cur = cur.next
        return None