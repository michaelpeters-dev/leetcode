# Problem: Top K Frequent Elements
# Number: 347
# Difficulty: Medium
# URL: https://leetcode.com/problems/top-k-frequent-elements/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 21.79 MB

                
        freq = {i:[] for i in range(len(nums) + 1)}        freq = {i:[] for i in range(len(nums) + 1)}

        for key, value in counter.items():        for key, value in counter.items():
            freq[value].append(key)            freq[value].append(key)
                
        result = []        result = []

        for f in range(len(freq) - 1, -1, -1):        for f in range(len(freq) - 1, -1, -1):
            for num in freq[f]:            for num in freq[f]:
                result.append(num)                result.append(num)
                if len(result) == k:                if len(result) == k:
                    return result                    return result
