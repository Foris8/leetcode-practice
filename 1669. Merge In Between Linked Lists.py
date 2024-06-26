# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:

        point1 = list1
        point2 = list1

        for _ in range(a - 1):
            point1 = point1.next

        for _ in range(b + 1):
            point2 = point2.next

        point1.next = list2

        tail = list2

        while tail.next:
            tail = tail.next

        tail.next = point2

        return list1
