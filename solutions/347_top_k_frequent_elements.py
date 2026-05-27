# Problem: Top K Frequent Elements
# Number: 347
# Difficulty: Medium
# URL: https://leetcode.com/problems/top-k-frequent-elements/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 0.00 MB

                
        freq_map = {i:[] for i in range(0, len(nums) + 1)}        freq_map = {i:[] for i in range(0, len(nums) + 1)}

        for key, value in counter.items():        for key, value in counter.items():
            freq_map[value].append(key)            freq_map[value].append(key)
                
        result = []        result = []

        for freq in range(len(freq_map)-1, -1, -1):        for freq in range(len(freq_map)-1, -1, -1):
            for num in freq_map[freq]:            for num in freq_map[freq]:
                result.append(num)                result.append(num)
            counter[num] = counter[num] + 1            counter[num] = counter[num] + 1
        for num in nums:        for num in nums:

                if len(result) == k:                if len(result) == k:
                    return result                    return result
