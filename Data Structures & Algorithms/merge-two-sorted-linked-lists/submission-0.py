# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # base cases
        if (list1 == None):
            return list2
        if (list2 == None):
            return list1
        
        head = None

        if (list2.val > list1.val):
            head = list1
            list1 = list1.next
            head.next = None
        else:
            head = list2
            list2 = list2.next
            head.next = None

        temp = head
        while(True):
            if (list1 == None):
                temp.next = list2
                break
            if (list2 == None):
                temp.next = list1
                break
            if (list2.val > list1.val):
                temp.next = list1
                list1 = list1.next
                temp = temp.next
            else:
                temp.next = list2
                list2 = list2.next
                temp=temp.next

        return head