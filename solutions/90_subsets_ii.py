# Problem: Subsets II
# Number: 90
# Difficulty: Medium
# URL: https://leetcode.com/problems/subsets-ii/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: N/A


            current.pop()            current.pop()

            # We skip, but as long as the number doesn't equal the previous one in the array            # We skip, but as long as the number doesn't equal the previous one in the array
            while i + 1<len(nums) and nums[i]==nums[i+1]:            while i + 1<len(nums) and nums[i]==nums[i+1]:
                    i += 1                    i += 1
            dfs(i+1, current)             dfs(i+1, current) 
        dfs(0, [])        dfs(0, [])
        return res        return res
            # We take, and don't skip            # We take, and don't skip
            current.append(nums[i])            current.append(nums[i])
            dfs(i + 1, current)            dfs(i + 1, current)
                        
                return                return
