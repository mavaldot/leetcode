# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 is None and list2 is None: return None
        if list1 is None: return list2
        if list2 is None: return list1
        head = ListNode()
        if (list1.val < list2.val):
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next

        curr = head

        while (True):

            if (list1 is None):
                curr.next = list2
                return head
            if (list2 is None):
                curr.next = list1
                return head

            if (list1.val < list2.val):
                curr.next = list1
                list1 = list1.next
                curr = curr.next
                curr.next = None                
            else:
                curr.next = list2
                list2 = list2.next
                curr = curr.next
                curr.next = None