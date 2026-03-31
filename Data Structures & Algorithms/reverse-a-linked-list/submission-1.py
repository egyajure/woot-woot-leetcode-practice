# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None):
            return head
        
        curNode = head.next
        prevNode = head
        prevNode.next = None

        while (curNode):
            temp = curNode.next
            curNode.next = prevNode
            prevNode = curNode
            curNode = temp
        
        return prevNode
        