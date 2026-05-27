# Problem: Same Tree
# Number: 100
# Difficulty: Easy
# URL: https://leetcode.com/problems/same-tree/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 0.00 MB

        :rtype: bool        :rtype: bool
        """        """
        def helper(p, q):        def helper(p, q):
            if (not p and not q):            if (not p and not q):
                        
            return helper(p.left, q.left) and helper(p.right, q.right)            return helper(p.left, q.left) and helper(p.right, q.right)
            if (not p and q) or (p and not q):            if (not p and q) or (p and not q):
                return False                 return False 
                return True                return True
        :type q: Optional[TreeNode]        :type q: Optional[TreeNode]
        :type p: Optional[TreeNode]        :type p: Optional[TreeNode]
            if p.val != q.val:            if p.val != q.val:
                return False                return False
                
        return helper(p, q)        return helper(p, q)
