# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev, curr = None, slow
        # slow is the middle point

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
