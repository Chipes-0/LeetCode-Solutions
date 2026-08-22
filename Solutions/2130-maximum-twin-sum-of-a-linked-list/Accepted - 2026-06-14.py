from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = [] 
        node = head 
        while node:
            arr.append(node.val)
            node = node.next
        N = len(arr)
        out = float("-inf")
        for i in range (N):
            out = max(out, arr[i] + arr[N -1 - i])
        return out