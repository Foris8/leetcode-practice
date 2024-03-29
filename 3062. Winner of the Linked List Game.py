# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        odd_team = 0
        even_team = 0

        while head and head.next:

            even_node = head
            odd_node = head.next

            if odd_node.val > even_node.val:
                odd_team += 1
            elif odd_node.val < even_node.val:
                even_team += 1

            head = head.next.next

        if odd_team == even_team:
            return "Tie"
        elif odd_team > even_team:
            return "Odd"
        else:
            return "Even"
