# Problem: Validate Binary Search Tree
# Number: 98
# Difficulty: Medium
# URL: https://leetcode.com/problems/validate-binary-search-tree/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 21.98 MB

class Solution {class Solution {
public:public:
    bool isValidBST(TreeNode* root) {    bool isValidBST(TreeNode* root) {
    }    }
 */ */
    bool isValidH(TreeNode* root, long left, long right) {    bool isValidH(TreeNode* root, long left, long right) {
        if (root == NULL) {        if (root == NULL) {
            return true;            return true;
        }        }

        if (root->val >= right || root->val <= left) return false;        if (root->val >= right || root->val <= left) return false;
        return isValidH(root->left, left, root->val) && isValidH(root->right, root->val, right);        return isValidH(root->left, left, root->val) && isValidH(root->right, root->val, right);
    }    }
        return isValidH(root, LONG_MIN, LONG_MAX);        return isValidH(root, LONG_MIN, LONG_MAX);
};};
