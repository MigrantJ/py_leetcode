"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        head = None
        last = None

        while curr1 is not None or curr2 is not None:
            if curr2 is None or (curr1 is not None and curr1.val <= curr2.val):
                if head is None:
                    head = curr1
                    last = head
                else:
                    last.next = curr1
                    last = curr1
                curr1 = curr1.next
            else:
                if head is None:
                    head = curr2
                    last = head
                else:
                    last.next = curr2
                    last = curr2
                curr2 = curr2.next
        return head
