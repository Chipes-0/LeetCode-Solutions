# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def balanceTree(start, end):
            if start > end:
                return None
            m = (start + end) // 2
            node = TreeNode(nums[m])

            node.left = balanceTree(start, m - 1)
            node.right = balanceTree(m + 1, end)

            return node
        
        return balanceTree(0, len(nums) - 1)