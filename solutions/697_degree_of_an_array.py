# Problem: Degree of an Array
# Number: 697
# Difficulty: Easy
# URL: https://leetcode.com/problems/degree-of-an-array/
# Submission Status: Accepted
# Runtime: 15 ms
# Memory: 19.18 MB

        last = {}        last = {}

        for i, num in enumerate(nums):        for i, num in enumerate(nums):
            if num not in freq:            if num not in freq:
                freq[num] = 1                freq[num] = 1
                first[num] = i                first[num] = i
            else:            else:
                freq[num] += 1                freq[num] += 1
            last[num] = i            last[num] = i

        degree = max(freq.values())        degree = max(freq.values())

        ans = float("inf")        ans = float("inf")
        for num in freq:        for num in freq:
            if freq[num] == degree:            if freq[num] == degree:
                ans = min(ans, last[num] - first[num] + 1)                ans = min(ans, last[num] - first[num] + 1)
                
        return ans        return ans

