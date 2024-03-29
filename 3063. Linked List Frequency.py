# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        freq = {}
        current = head
        freq_head = None

        while current:
            if current.val in freq:
                freq_node = freq[current.val]
                freq_node.val += 1

            else:
                new_freq_node = ListNode(1, freq_head)
                freq[current.val] = new_freq_node
                freq_head = new_freq_node

            current = current.next
        return freq_head
