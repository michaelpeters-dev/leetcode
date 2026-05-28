# Problem: 3Sum
# Number: 15
# Difficulty: Medium
# URL: https://leetcode.com/problems/3sum/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 0.00 MB

        result = []        result = []
        for i in range(len(nums) - 2):        for i in range(len(nums) - 2):
            low = i + 1            low = i + 1
            high = len(nums) - 1            high = len(nums) - 1
            while low < high:            while low < high:

                if summation == 0:                if summation == 0:

                    result.append([nums[i], nums[low], nums[high]])                    result.append([nums[i], nums[low], nums[high]])
                elif summation > 0:                elif summation > 0:
            if i>0 and nums[i]==nums[i-1]:            if i>0 and nums[i]==nums[i-1]:
                continue                continue

                summation = nums[i] + nums[low] + nums[high]                summation = nums[i] + nums[low] + nums[high]
                    high -= 1                    high -= 1
                    while low < high and nums[low] == nums[low-1]:                    while low < high and nums[low] == nums[low-1]:
                        low += 1                        low += 1
                    while high > low and nums[high] == nums[high+1]:                    while high > low and nums[high] == nums[high+1]:
                        high -= 1                        high -= 1
                    low += 1                    low += 1
                    high -= 1                     high -= 1 

                else:                else:
                    low += 1                    low += 1
                
        return result        return result
