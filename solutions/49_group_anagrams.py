# Problem:    49. Group Anagrams
# Difficulty: Medium
# Language:   Python3
# Runtime:    13 ms
# Memory:     21.9 MB
# Solved:     2026-10-23
# URL:        https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        store = defaultdict(list) # stortedstr -> [strs]

        for string in strs:
            key = ''.join(sorted(string))

            store[key].append(string)
        
        result = []
        for key, value in store.items():
            result.append(value)
        
        return result
