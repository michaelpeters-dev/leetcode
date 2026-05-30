# Problem: Invert Binary Tree
# Number: 226
# Difficulty: Easy
# URL: https://leetcode.com/problems/invert-binary-tree/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: N/A

/**/**
 * Definition for a binary tree node. * Definition for a binary tree node.
 * struct TreeNode { * struct TreeNode {
 *     int val; *     int val;
 *     TreeNode *left; *     TreeNode *left;
 *     TreeNode *right; *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {} *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {} *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {} *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * }; * };
 */ */
class Solution {class Solution {
public:public:
    void helper(TreeNode* root) {    void helper(TreeNode* root) {
        if (root == nullptr) {        if (root == nullptr) {
            return;            return;
        }        }

        swap(root->left, root->right);        swap(root->left, root->right);
        helper(root->left);        helper(root->left);
        helper(root->right);        helper(root->right);
    }    }
    TreeNode* invertTree(TreeNode* root) {    TreeNode* invertTree(TreeNode* root) {
        helper(root);        helper(root);
        return root;        return root;
    }    }

};};
