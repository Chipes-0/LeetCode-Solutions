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
    bool findNode(TreeNode* node, int value, vector<char>& arr){
        if (node == nullptr) return 0;
        if (node->val == value) return 1;
        
        arr.push_back('L');
        if (findNode(node->left, value, arr)){
            return true;
        }
        arr.pop_back();
        arr.push_back('R');
        if (findNode(node->right, value, arr)){
            return true;
        }
        arr.pop_back();
        return false;
    }
    string getDirections(TreeNode* root, int startValue, int destValue) {
        vector<char> sr;
        vector<char> dr;
        findNode(root, startValue, sr);
        findNode(root, destValue, dr);
        string out = "";
        int i;
        for(i = 0; i < sr.size(); i++){
            if( i == dr.size() or sr[i] != dr[i]) break;
        }
        int j = i;
        while (i < sr.size()){
            out += "U";
            i++;
        }
        while (j < dr.size()){
            out += dr[j];
            j++;
        }
        return out;
    }
};