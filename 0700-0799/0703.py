"""
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.
"""

from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.minheap = []
        self.length = k

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        self.minheap.append(val)
        # heap up
        curr_index = len(self.minheap) - 1
        while curr_index > 0:
            # check if parent is larger
            parent_index = (curr_index - 1) // 2
            if self.minheap[parent_index] > val:
                self.minheap[parent_index], self.minheap[curr_index] = (
                    self.minheap[curr_index],
                    self.minheap[parent_index],
                )
                curr_index = parent_index
            else:
                break
        if len(self.minheap) > self.length:
            self.minheap[0], self.minheap[self.length] = (
                self.minheap[self.length],
                self.minheap[0],
            )
            self.minheap.pop()
            # heap down
            curr_index = 0
            while curr_index < self.length - 1:
                left_index = curr_index * 2 + 1
                right_index = left_index + 1
                smallest_index = left_index
                if (
                    right_index <= self.length - 1
                    and self.minheap[left_index] > self.minheap[right_index]
                ):
                    smallest_index = right_index
                if (
                    smallest_index <= self.length - 1
                    and self.minheap[curr_index] > self.minheap[smallest_index]
                ):
                    self.minheap[curr_index], self.minheap[smallest_index] = (
                        self.minheap[smallest_index],
                        self.minheap[curr_index],
                    )
                    curr_index = smallest_index
                else:
                    break
        return self.minheap[0]
