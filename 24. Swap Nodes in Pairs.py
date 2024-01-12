# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(next=head)
        curr = dummy_head

        while curr.next and curr.next.next:
            next_node = curr.next
            next_next_node = curr.next.next
            temp = curr.next.next.next

            curr.next = next_next_node
            next_next_node.next = next_node
            next_node.next = temp
            curr = next_node

        return dummy_head.next
