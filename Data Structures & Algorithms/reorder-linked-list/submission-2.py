# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None or head.next.next is None:
            return

        # 1. Find the middle (slow stops at the end of first half)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Split the list into two halves
        second = slow.next      # start of second half
        slow.next = None        # break the list so no overlap

        # 3. Reverse the second half
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        second = prev           # now second points to reversed half

        # 4. Merge two halves
        first = head
        while second:
            # store next nodes
            tmp1, tmp2 = first.next, second.next
            # link nodes alternately
            first.next = second
            second.next = tmp1
            # move pointers forward
            first, second = tmp1, tmp2

