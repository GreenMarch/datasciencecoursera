# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        h = [(l.val, idx) for idx, l in enumerate(lists) if l]
        heapq.heapify(h)
        head = cur = ListNode(None)
        while h:
            val, idx = heapq.heappop(h)
            cur.next = ListNode(val)
            cur = cur.next
            node = lists[idx] = lists[idx].next
            if node:
                heapq.heappush(h, (node.val, idx))
        return head.next
        
"""
23. Merge k Sorted Lists
Hard

3166

208

Favorite

Share
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from heapq import heappop, heappush


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        values, head, pointer = [], None, None

        for l in lists:
            while l:
                heappush(values, l.val)
                l = l.next
        print("values", values)
        while values:
            if head == None:
                head = ListNode(heappop(values))
                pointer = head
            else:
                pointer.next = ListNode(heappop(values))
                pointer = pointer.next

        return head