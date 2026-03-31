# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if (head is None):
            return False

        slow = head
        fast = head.next

        while(fast is not None):
            slow = slow.next
            fast = fast.next
            if (slow == fast):
                return True
            if (fast == None):
                return False
            fast = fast.next
        return False
        