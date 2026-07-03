# Problem: Same Tree
# Number: 100
# Difficulty: Easy
# URL: https://leetcode.com/problems/same-tree/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: N/A

        }        }
            return;            return;

        if (first->val != second->val) {        if (first->val != second->val) {
            same = false;            same = false;
            return;            return;
        if (first == nullptr && second == nullptr) {        if (first == nullptr && second == nullptr) {
    void preOrder(TreeNode* first, TreeNode* second) {    void preOrder(TreeNode* first, TreeNode* second) {
    bool same = true;    bool same = true;
 * }; * };
 */ */
class Solution {class Solution {
public:public:
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {} *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {} *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {} *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode *right; *     TreeNode *right;
 *     int val; *     int val;
 *     TreeNode *left; *     TreeNode *left;
 * struct TreeNode { * struct TreeNode {
 * Definition for a binary tree node. * Definition for a binary tree node.

        if (first == nullptr || second == nullptr) {        if (first == nullptr || second == nullptr) {
            return;            return;
        }        }
            same = false;            same = false;
