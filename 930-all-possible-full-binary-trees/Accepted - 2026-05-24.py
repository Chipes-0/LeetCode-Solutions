# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        # memorization
        dp = {}
        # if n is even, there is no possible full binary tree 
        if n % 2 == 0:
            return [] 
        def recursiveSolution(n: int) -> List[Optional[TreeNode]]:
            # base case
            if n == 1:
                return [TreeNode(0)]
            if n in dp:
                return dp[n]
            # array with the possible full binary tree at n
            ans = []

            # recursive case goes from all odd number from 1 to n - 2
            # 7 -> 1-5, 3-3, 5-1
            for i in range(n - 1, 0, -2):
                # get the left and right tree
                leftTree, rightTree = recursiveSolution(i - 1), recursiveSolution(n - i)
                for left in leftTree:
                    for right in rightTree:
                        # build the possible trees for lest and right side of the node
                        ans.append(TreeNode(0, left, right))    
            # add to the memorization and return
            dp[n] = ans
            return dp[n]
        return recursiveSolution(n)
