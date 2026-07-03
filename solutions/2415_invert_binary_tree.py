# Problem: Reverse Odd Levels of Binary Tree
# Number: 2415
# Difficulty: Unknown
# URL: https://leetcode.com/problems/invert-binary-tree/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 12.48 MB

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
    TreeNode* invertTree(TreeNode* root) {    TreeNode* invertTree(TreeNode* root) {
        if (root == nullptr) {        if (root == nullptr) {
            return nullptr;            return nullptr;
        }        }

        TreeNode* left = root->left;        TreeNode* left = root->left;
        TreeNode* right = root->right;        TreeNode* right = root->right;

        root->left = right;        root->left = right;
        root->right = left;        root->right = left;

        invertTree(left);        invertTree(left);
