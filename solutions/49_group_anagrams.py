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

        store = defaultdict(list)        store = defaultdict(list)

        for string in strs:        for string in strs:
            sorted_string = "".join(sorted(string))            sorted_string = "".join(sorted(string))
            store[sorted_string].append(string)            store[sorted_string].append(string)
                
        result = []        result = []
        for key, value in store.items():        for key, value in store.items():
                
            result.append(value)            result.append(value)
        return result        return result
