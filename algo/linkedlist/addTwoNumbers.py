# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = curr = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, v = divmod(v1 + v2 + carry, 10)
            curr.next = ListNode(v)
            curr = curr.next
        return head.next
"""
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        # dummy head
        head = curr = ListNode(0)
        while l1 or l2:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            curr.next = ListNode(val % 10)
            curr = curr.next
            carry = int((val - val % 10) / 10)
        if carry > 0:
            curr.next = ListNode(carry)
        return head.next
"""
