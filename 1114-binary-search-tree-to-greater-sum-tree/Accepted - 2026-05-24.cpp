/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int dfs(TreeNode* node, int c) {
        int r_sum = 0, l_sum = 0;
        if (node->right){
            c = dfs(node->right, c);
        }
        node->val += c;
        if (node->left){
            l_sum = dfs(node->left, node->val);
            return l_sum;
        }
        return node->val;
    }

    TreeNode* bstToGst(TreeNode* root) {
        dfs(root, 0);
        return root;
    }
};