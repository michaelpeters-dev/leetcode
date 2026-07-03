# Problem: Subtree of Another Tree
# Number: 572
# Difficulty: Easy
# URL: https://leetcode.com/problems/subtree-of-another-tree/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 0.00 MB

        }        }

        preOrder(first->left, second->left);        preOrder(first->left, second->left);
        preOrder(first->right, second->right);        preOrder(first->right, second->right);
    }    }

    bool isSame(TreeNode* a, TreeNode* b) {    bool isSame(TreeNode* a, TreeNode* b) {
        same = true;        same = true;
        preOrder(a, b);        preOrder(a, b);
        return same;        return same;
    }    }


    bool isSubtree(TreeNode* root, TreeNode* subRoot) {    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        if (root == nullptr) {        if (root == nullptr) {
            return false;            return false;
        }        }

        if (isSame(root, subRoot)) return true;        if (isSame(root, subRoot)) return true;
        return (isSubtree(root->left, subRoot) || isSubtree(root->right, subRoot));        return (isSubtree(root->left, subRoot) || isSubtree(root->right, subRoot));
    }    }
};};
