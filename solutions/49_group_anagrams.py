# Problem: Group Anagrams
# Number: 49
# Difficulty: Medium
# URL: https://leetcode.com/problems/group-anagrams/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = {}
        for string in strs:
            sorted_str = sorted(string)
            temp = ""
            for letter in sorted_str:
                temp += letter
            if temp in anagrams:
                anagrams[temp].append(string)
            else:
                anagrams[temp] = [string]
        results = []
        for value in anagrams.values():
            results.append(value)
        return results
