# Problem: Trapping Rain Water
# Number: 42
# Difficulty: Hard
# URL: https://leetcode.com/problems/trapping-rain-water/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 19.51 MB

            return 0            return 0
                
        l, r = 0, len(height)-1        l, r = 0, len(height)-1
        leftMax, rightMax = height[l], height[r]        leftMax, rightMax = height[l], height[r]
        res = 0        res = 0

        while l<r:        while l<r:
            if leftMax < rightMax:            if leftMax < rightMax:
                l += 1                l += 1
            else:            else:
                leftMax = max(leftMax, height[l])                leftMax = max(leftMax, height[l])
                r -= 1                r -= 1
                res += leftMax - height[l]                res += leftMax - height[l]
                rightMax = max(rightMax, height[r])                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]                res += rightMax - height[r]
        return res        return res
