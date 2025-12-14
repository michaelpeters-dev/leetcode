# Problem: Combination Sum
# Number: 39
# Difficulty: Medium
# URL: https://leetcode.com/problems/combination-sum/
# Submission Status: Accepted
# Runtime: 11 ms
# Memory: 17.81 MB

        res = []        res = []

        def dfs(total, path, i):        def dfs(total, path, i):
            if total==0:            if total==0:
                res.append(path)                res.append(path)
                return                return
            if total<0:            if total<0:
                return                return
            if i==len(candidates):            if i==len(candidates):
                return                return
                        
            dfs(total, path, i + 1)            dfs(total, path, i + 1)
        dfs(target, [], 0)        dfs(target, [], 0)
        return res        return res
            dfs(total - candidates[i], path + [candidates[i]], i)            dfs(total - candidates[i], path + [candidates[i]], i)
                        
                        
                
