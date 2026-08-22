# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        arraylist = []
        while head != None:
            arraylist.append(head.val)
            head = head.next
        max_sum = 0
        for i in range(len(arraylist) / 2):
            sum = arraylist[i] + arraylist[len(arraylist) - 1 - i]
            if sum > max_sum:
                max_sum = sum
        return max_sum