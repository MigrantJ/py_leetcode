"""
Given the head of a singly linked list, reverse the list, and return the head of the reversed list.
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        last = None
        while curr is not None:
            temp = curr.next
            curr.next = last
            last = curr
            curr = temp
        return last
