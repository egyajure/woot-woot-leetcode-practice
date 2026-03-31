# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # first, we loop through the list to get the length

        numNodes = 0
        counter = head
        while(counter):
            numNodes += 1
            counter = counter.next
        
        # then, once we have the total number of nodes
        # total - n - 1 = how far we have to go 
        # this will bring us to the one before, at which point we can make it point to next.next
        
        stepsToTravel = numNodes - n - 1
        if (stepsToTravel == -1):
            return head.next

        traveller = head

        for i in range(stepsToTravel):
            traveller = traveller.next
        
        traveller.next = traveller.next.next
        return head