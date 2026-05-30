# Problem: Maximum Depth of Binary Tree
# Number: 104
# Difficulty: Easy
# URL: https://leetcode.com/problems/maximum-depth-of-binary-tree/
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
    int maxDepth(TreeNode* root) {    int maxDepth(TreeNode* root) {
        return helper(root);        return helper(root);
    int helper(TreeNode* root) {    int helper(TreeNode* root) {

        if (root == nullptr) {        if (root == nullptr) {
    }    }
            return 0;            return 0;
        }        }
    }    }

        return max(helper(root->left), helper(root->right)) + 1;        return max(helper(root->left), helper(root->right)) + 1;
};};
