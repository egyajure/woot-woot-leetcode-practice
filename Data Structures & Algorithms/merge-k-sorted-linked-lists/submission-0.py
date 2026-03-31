# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    

    def merge(self, head: ListNode, listToMerge: ListNode) -> ListNode:
        dummy = ListNode(1, None)
        curr = dummy
        while (head and listToMerge):
            if (head.val < listToMerge.val):
                curr.next = head
                head = head.next
            else:
                curr.next = listToMerge
                listToMerge = listToMerge.next
            curr = curr.next
        if (head is None):
            curr.next = listToMerge
        else:
            curr.next = head
        
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # simplist idea may be easiest
        # make a dummy node and return dummy.next
        
        # phseudocode: find the smallest out of the k lists, add to dummynode, keep going
        # WRONG ^ this would work but finding the smallest out of the lists everytime would not be good

        if (len(lists) == 0):
            return None
        if (len(lists) == 1):
            return lists[0]

        head = lists[0]

        for i in range (1, len(lists)):
            listToMerge = lists[i]
            head = self.merge(head, listToMerge)

        return head
        