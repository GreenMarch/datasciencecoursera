# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def get_result(self, head, stack, index):
        if head == None:
            return
        stack.append((head, index))
        self.get_result(head.next, stack, index + 1)

    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack = []
        self.get_result(head, stack, 0)
        visited = set()
        temp = head
        prev = None
        index = 0
        while temp and index not in visited:
            visited.add(index)
            next = temp.next
            k, k_index = stack.pop(-1)
            visited.add(k_index)
            k.next = None
            if prev != None:
                prev.next = temp
            if index == k_index:
                break
            temp.next = k
            prev = k
            temp = next
            index += 1
        return head

"""
143. Reorder List
Medium

1421

98

Add to List

Share
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
"""