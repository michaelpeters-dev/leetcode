# Problem: Kth Smallest Element in a BST
# Number: 230
# Difficulty: Medium
# URL: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 0.00 MB

        if (counter == k) {        if (counter == k) {
            dummy->val = curr->val;            dummy->val = curr->val;
        inOrder(curr->left, dummy, k);        inOrder(curr->left, dummy, k);

        }        }
            return nullptr;            return nullptr;
        if (curr == nullptr) {        if (curr == nullptr) {
    TreeNode* inOrder(TreeNode* curr, TreeNode* dummy, int k) {    TreeNode* inOrder(TreeNode* curr, TreeNode* dummy, int k) {
    static inline int counter;    static inline int counter;
public:public:
class Solution {class Solution {
        counter++;        counter++;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {} *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {} *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {} *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * }; * };
 */ */
 *     TreeNode *left; *     TreeNode *left;
 *     TreeNode *right; *     TreeNode *right;
 * struct TreeNode { * struct TreeNode {
 *     int val; *     int val;
 * Definition for a binary tree node. * Definition for a binary tree node.
/**/**
