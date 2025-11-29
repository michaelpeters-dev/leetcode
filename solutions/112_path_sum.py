# Problem: Path Sum
# Number: 112
# Difficulty: Easy
# URL: https://leetcode.com/problems/path-sum/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution(object):
    def hasPathSum(self, root, targetSum):
        path = []
        def leafPath(root, path):
            if not root:
                return False

            path.append(root.val)

            if not root.left and not root.right and sum(path)==targetSum:
                return True
            if leafPath(root.left, path) or leafPath(root.right, path):
                return True

            path.pop()
            return False

        return leafPath(root, path)
