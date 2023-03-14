# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        hp = []
        for l in lists:
            cur = l
            while cur is not None:
                heapq.heappush(hp, cur.val)
                cur = cur.next

        if len(hp) < 1:
            return None
        head = ListNode()
        first = heapq.heappop(hp)
        cur = ListNode(first)
        prev = cur
        head.next = prev
        while hp:
            n = heapq.heappop(hp)
            cur = ListNode(n)
            prev.next = cur
            prev = cur
        return head.next