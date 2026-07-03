# Problem: Diameter of Binary Tree
# Number: 543
# Difficulty: Easy
# URL: https://leetcode.com/problems/diameter-of-binary-tree/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 0.00 MB

public:public:
    int diameterOfBinaryTree(TreeNode* root) {    int diameterOfBinaryTree(TreeNode* root) {
    int findMax(TreeNode* node) {    int findMax(TreeNode* node) {

        if (node == nullptr) {        if (node == nullptr) {
    }    }
            return 0;            return 0;
        }        }

        return max(findMax(node->left), findMax(node->right)) + 1;        return max(findMax(node->left), findMax(node->right)) + 1;
        if (root->left != nullptr && root->right != nullptr) {        if (root->left != nullptr && root->right != nullptr) {
        int maximum = 0;        int maximum = 0;
        } else if (root -> left != nullptr) {        } else if (root -> left != nullptr) {
            maximum = findMax(root->left) + findMax(root->right);            maximum = findMax(root->left) + findMax(root->right);
            maximum = findMax(root->left);            maximum = findMax(root->left);
        } else if (root -> right != nullptr) {        } else if (root -> right != nullptr) {
            maximum = findMax(root->right);            maximum = findMax(root->right);
        }        }
    }    }
            return max(max(diameterOfBinaryTree(root->left), diameterOfBinaryTree(root->right)), maximum);            return max(max(diameterOfBinaryTree(root->left), diameterOfBinaryTree(root->right)), maximum);
            return max(maximum, diameterOfBinaryTree(root->left));            return max(maximum, diameterOfBinaryTree(root->left));
            return max(maximum, diameterOfBinaryTree(root->right));            return max(maximum, diameterOfBinaryTree(root->right));
class Solution {class Solution {
 */ */

        return maximum;        return maximum;
