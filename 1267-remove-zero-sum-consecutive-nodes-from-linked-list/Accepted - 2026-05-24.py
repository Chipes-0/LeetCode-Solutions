# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prefix_sum = []
        current = head
        total_sum = 0
        seen = []
        while current:
            total_sum += current.val
            prefix_sum.append(total_sum)
            if total_sum in seen:
                curr_total = total_sum
                curr_total -= prefix_sum.pop()
                seen.pop()
                while curr_total != total_sum:
                    
                    curr_total -= prefix_sum.pop()
            else:
                seen.append(ptotal_sum)
            current = current.next
        print(prefix_sum)
        return head