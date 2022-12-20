class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        result = ListNode()
        head.next = result
        carry = 0

        while True:
            sum = 0
            if l1 is not None:
                sum += l1.val
                l1 = l1.next
            if l2 is not None:
                sum += l2.val
                l2 = l2.next
            sum += carry
            carry = 0
            if (sum >= 10): 
                sum = sum % 10
                carry = 1
            tmp = ListNode(sum)
            result.val = sum
            if not l1 and not l2:
                break
            result.next = ListNode()
            result = result.next

        if (carry):
            result.next = ListNode(1)

        return head.next