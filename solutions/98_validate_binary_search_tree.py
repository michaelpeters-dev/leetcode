# Problem: Validate Binary Search Tree
# Number: 98
# Difficulty: Medium
# URL: https://leetcode.com/problems/validate-binary-search-tree/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: N/A

 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {} *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {} *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * }; * };
 */ */
class Solution {class Solution {
public:public:
    bool helper(TreeNode* root, long leftMin, long rightMax)    bool helper(TreeNode* root, long leftMin, long rightMax)
        if (root == nullptr) {        if (root == nullptr) {
            return true;            return true;
        }        }
        if (root->val <= leftMin || root->val >= rightMax) {        if (root->val <= leftMin || root->val >= rightMax) {
            return false;            return false;
        }        }

    {    {
 *     TreeNode *right; *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {} *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
        return helper(root->left, leftMin, root->val) && helper(root->right, root->val, rightMax);        return helper(root->left, leftMin, root->val) && helper(root->right, root->val, rightMax);
    }    }

    bool isValidBST(TreeNode* root) {    bool isValidBST(TreeNode* root) {
        return helper(root, LONG_MIN, LONG_MAX);        return helper(root, LONG_MIN, LONG_MAX);
    }    }
