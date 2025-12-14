# Problem: Trapping Rain Water
# Number: 42
# Difficulty: Hard
# URL: https://leetcode.com/problems/trapping-rain-water/
# Submission Status: Accepted
# Runtime: 20 ms
# Memory: 19.51 MB

            maxL[i] = temp_max            maxL[i] = temp_max
            temp_max = max(temp_max, height[i])            temp_max = max(temp_max, height[i])
                
        temp_max = 0        temp_max = 0
        for i in range(len(height)-1, -1, -1):        for i in range(len(height)-1, -1, -1):
            maxR[i] = temp_max            maxR[i] = temp_max
            temp_max = max(temp_max, height[i])            temp_max = max(temp_max, height[i])
                
        res = 0        res = 0
        for i in range(len(height)):        for i in range(len(height)):
            min_amount = min(maxL[i], maxR[i])            min_amount = min(maxL[i], maxR[i])
            if min_amount-height[i]>0:            if min_amount-height[i]>0:
                res += min_amount-height[i]                res += min_amount-height[i]
        return res        return res
