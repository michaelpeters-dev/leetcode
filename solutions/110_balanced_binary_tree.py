# Problem: Balanced Binary Tree
# Number: 110
# Difficulty: Easy
# URL: https://leetcode.com/problems/balanced-binary-tree/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 0.00 MB

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
    bool balanced = true;    bool balanced = true;
    int calculate(TreeNode* node) {    int calculate(TreeNode* node) {
        if (node == nullptr) {        if (node == nullptr) {
            return 0;            return 0;
        }        }

        int leftHeight = calculate(node->left);        int leftHeight = calculate(node->left);
        int rightHeight = calculate(node->right);        int rightHeight = calculate(node->right);

        if (abs(leftHeight - rightHeight) > 1) {        if (abs(leftHeight - rightHeight) > 1) {
            balanced = false;            balanced = false;
        }        }

        return max(leftHeight, rightHeight) + 1;        return max(leftHeight, rightHeight) + 1;
    }    }
