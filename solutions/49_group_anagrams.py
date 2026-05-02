# Problem: Group Anagrams
# Number: 49
# Difficulty: Medium
# URL: https://leetcode.com/problems/group-anagrams/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: N/A

class Solution(object):class Solution(object):
    def groupAnagrams(self, strs):    def groupAnagrams(self, strs):
        """        """
        :type strs: List[str]        :type strs: List[str]
        :rtype: List[List[str]]        :rtype: List[List[str]]
        """        """

        store = {}        store = {}
        for string in strs:        for string in strs:
            temp = "".join(sorted(string))            temp = "".join(sorted(string))
            if temp in store:            if temp in store:
                store[temp].append(string)                store[temp].append(string)
            else:            else:
                store[temp] = []                store[temp] = []
        result = []        result = []
        for key, value in store.items():        for key, value in store.items():
            result.append(value)            result.append(value)
                
                store[temp].append(string)                store[temp].append(string)
        return result        return result
