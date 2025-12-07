# Problem: Diameter of Binary Tree
# Number: 543
# Difficulty: Easy
# URL: https://leetcode.com/problems/diameter-of-binary-tree/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: N/A

        #                4     5        #                4     5
        # max = 0        # max = 0
        # 1 + max of both children each time        # 1 + max of both children each time
        maximum = [0]        maximum = [0]
        def dfs(root):        def dfs(root):
            if not root:            if not root:
                return 0                return 0
                        
            max_left_branch = dfs(root.left)            max_left_branch = dfs(root.left)
            max_right_branch = dfs(root.right)            max_right_branch = dfs(root.right)

            maximum[0] = max(maximum[0], curr_max)            maximum[0] = max(maximum[0], curr_max)
            return 1 + max(max_left_branch, max_right_branch)            return 1 + max(max_left_branch, max_right_branch)
            curr_max = max_left_branch + max_right_branch            curr_max = max_left_branch + max_right_branch
        dfs(root)        dfs(root)
        return maximum[0]        return maximum[0]
                        
                                        
                
