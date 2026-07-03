# Problem: Lowest Common Ancestor of a Binary Search Tree
# Number: 235
# Difficulty: Medium
# URL: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 0.00 MB

 */ */

class Solution {class Solution {
public:public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
    // We want continue moving downward until we have: p < root < q    // We want continue moving downward until we have: p < root < q
        if (p->val > root->val && q->val > root->val) {        if (p->val > root->val && q->val > root->val) {
        } else if (p->val < root->val && q->val < root->val) {        } else if (p->val < root->val && q->val < root->val) {
            return lowestCommonAncestor(root->left, p, q);            return lowestCommonAncestor(root->left, p, q);
        } else {        } else {
        }        }
        if (p->val > q->val) {        if (p->val > q->val) {
            swap(p, q);            swap(p, q);
        }        }

    }    }
 * }; * };
            return lowestCommonAncestor(root->right, p, q);            return lowestCommonAncestor(root->right, p, q);
            return root;            return root;
};};
