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
    void divideTree(TreeNode* node, vector<TreeNode*>& list, vector<int>& to_delete){
        if (node->left != nullptr) {
            if(find(to_delete.begin(), to_delete.end(),node->left->val) != to_delete.end()){
                to_delete.erase(remove(to_delete.begin(), to_delete.end(), node->left->val), to_delete.end());
                if(node->left->left != nullptr){
                    list.push_back(node->left->left);
                }
                if(node->left->right != nullptr){
                    list.push_back(node->left->right);
                }
                node->left = nullptr;
            } else {
                divideTree(node->left, list, to_delete);
            }
        }
        if (node->right != nullptr) {
            if (find(to_delete.begin(), to_delete.end(),node->right->val) != to_delete.end()){
                to_delete.erase(remove(to_delete.begin(), to_delete.end(), node->right->val), to_delete.end());
                if(node->right->left != nullptr){
                    list.push_back(node->right->left);
                }
                if(node->right->right != nullptr){
                    list.push_back(node->right->right);
                }
                node->right = nullptr;
            } else {
                divideTree(node->right, list, to_delete);
            }
        }
    }

    vector<TreeNode*> delNodes(TreeNode* root, vector<int>& to_delete) {
       vector<TreeNode*> out;
       out.push_back(root);
       int i = 0;
       while (i < out.size()){
        divideTree(out[i], out, to_delete);
        i++;
       }
       return out;      
    }
};