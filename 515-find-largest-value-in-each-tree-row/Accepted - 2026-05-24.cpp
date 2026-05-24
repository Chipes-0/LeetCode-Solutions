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
#include <limits.h>

class Solution {
public:
    void dfs(TreeNode* node, int depth, vector<int>& out){
        if(node == nullptr) return;
        if(out.size() <= depth){
            out.push_back(INT_MIN);
        }
        out[depth] = max(out[depth], node->val);
        dfs(node->left, depth + 1, out);
        dfs(node->right, depth + 1, out);
    }

    vector<int> largestValues(TreeNode* root) {
        vector<int> out;
        dfs(root, 0, out);
        return out;
    }
};