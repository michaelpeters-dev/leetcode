# Problem: Group Anagrams
# Number: 49
# Difficulty: Medium
# URL: https://leetcode.com/problems/group-anagrams/
# Submission Status: Accepted
# Runtime: 19 ms
# Memory: 16.74 MB

class Solution(object):class Solution(object):
    def groupAnagrams(self, strs):    def groupAnagrams(self, strs):
        """        """
        :type strs: List[str]        :type strs: List[str]
        :rtype: List[List[str]]        :rtype: List[List[str]]
        """        """
        result = {}        result = {}

        for string in strs:        for string in strs:
            temp = "".join(sorted(string))            temp = "".join(sorted(string))
            if temp in result:            if temp in result:
                result[temp].append(string)                result[temp].append(string)
            else:            else:
                result[temp] = [string]                result[temp] = [string]
                
        return_list = []        return_list = []
        for key, value in result.items():        for key, value in result.items():
            return_list.append(value)            return_list.append(value)
        return return_list        return return_list
                                
