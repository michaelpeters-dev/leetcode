# Problem: 3Sum
# Number: 15
# Difficulty: Medium
# URL: https://leetcode.com/problems/3sum/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: N/A

                continue                continue
                        
            l, r = i + 1, len(nums)-1            l, r = i + 1, len(nums)-1
            while l < r:            while l < r:
                threeSum = a + nums[l] + nums[r]                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:                if threeSum > 0:
                    r -= 1                    r -= 1
                elif threeSum < 0:                elif threeSum < 0:
                    l += 1                    l += 1
                else:                else:
                    res.append([a, nums[l], nums[r]])                    res.append([a, nums[l], nums[r]])
                    l += 1                    l += 1
                    while nums[l]==nums[l-1] and l<r:                    while nums[l]==nums[l-1] and l<r:
                        l += 1                        l += 1
        return res        return res
