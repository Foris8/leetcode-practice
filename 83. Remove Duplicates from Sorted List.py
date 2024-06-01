# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()

        dummy_head = ListNode()
        dummy_head.next = head

        prev = dummy_head

        while head:
            if head.val not in seen:
                seen.add(head.val)
                prev = head
                head = head.next
            else:
                prev.next = head.next
                head = head.next

        return dummy_head.next
