/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) 
    {
        if(root == NULL)
        {
            return NULL;
        }
        TreeNode* res = new TreeNode(root->val);
        if(root->right)
        {
            res->left = invertTree(root->right);
        }
        if(root->left)
        {
            res->right = invertTree(root->left);
        }
        
        return res;
    }
};
