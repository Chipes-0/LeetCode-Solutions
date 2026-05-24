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
#include <vector>

using namespace std;

class Solution {
public:
    void storeNodes(TreeNode* node, vector<int>& v){
        if (node->left){
            storeNodes(node->left, v);
        }
        v.push_back(node->val);
        if (node->right){
            storeNodes(node->right, v);
        }
    }

    TreeNode* buildBST(int s, int e, vector<int>& v){
        int m = (s + e) / 2;
        if (s > e) {
            return nullptr;
        }
        TreeNode* left = buildBST(s, m - 1, v);
        TreeNode* right = buildBST(m + 1, e, v);
        return new TreeNode(v[m], left, right);
    }


    TreeNode* balanceBST(TreeNode* root) {
        vector<int> v;
        storeNodes(root, v);
        return buildBST(0, v.size() - 1, v);
    }
};