# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.total = 0
        self.head = head
        cur = head
        while (cur):
            self.total += 1
            cur = cur.next

    def getRandom(self) -> int:
        num = random.randint(0, self.total - 1)
        cur = self.head
        while num > 0:
            cur = cur.next
            num -= 1

        return cur.val
            


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()