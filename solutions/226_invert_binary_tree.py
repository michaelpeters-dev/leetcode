# Problem: Invert Binary Tree
# Number: 226
# Difficulty: Easy
# URL: https://leetcode.com/problems/invert-binary-tree/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 12.34 MB

        """        """
        :type root: Optional[TreeNode]        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]        :rtype: Optional[TreeNode]
        """        """
            if root == None:            if root == None:
        def helper(root):        def helper(root):
                return root                return root
            helper(root.right)            helper(root.right)

        helper(root)        helper(root)
        return root        return root
    def invertTree(self, root):    def invertTree(self, root):
            helper(root.left)            helper(root.left)
            temp = root.left            temp = root.left
            root.left = root.right            root.left = root.right
            root.right = temp            root.right = temp
                        
                
