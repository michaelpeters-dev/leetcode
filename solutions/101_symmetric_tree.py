# Problem: Symmetric Tree
# Number: 101
# Difficulty: Easy
# URL: https://leetcode.com/problems/symmetric-tree/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: N/A

    }    }
        if (root==nullptr) return true;        if (root==nullptr) return true;
    bool isSymmetric(TreeNode* root) {    bool isSymmetric(TreeNode* root) {
public:public:
        return mirror(root->left, root->right);        return mirror(root->left, root->right);

    bool mirror(TreeNode* left, TreeNode* right) {    bool mirror(TreeNode* left, TreeNode* right) {
        if (left==nullptr && right==nullptr) return true;        if (left==nullptr && right==nullptr) return true;
    }    }
        if (left==nullptr || right==nullptr) return false;        if (left==nullptr || right==nullptr) return false;
        if (left->val != right->val) return false;        if (left->val != right->val) return false;

        return mirror(left->left, right->right) && mirror(left->right, right->left);        return mirror(left->left, right->right) && mirror(left->right, right->left);
};};
