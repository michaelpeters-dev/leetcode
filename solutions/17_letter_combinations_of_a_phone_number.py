# Problem: Letter Combinations of a Phone Number
# Number: 17
# Difficulty: Medium
# URL: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 17.74 MB

class Solution:class Solution:
    def letterCombinations(self, digits: str) -> List[str]:    def letterCombinations(self, digits: str) -> List[str]:
        representations = {"2":["a", "b", "c"], "3":["d", "e", "f"], "4":["g", "h", "i"], "5":["j", "k", "l"], "6":["m", "n",         representations = {"2":["a", "b", "c"], "3":["d", "e", "f"], "4":["g", "h", "i"], "5":["j", "k", "l"], "6":["m", "n", 
"o"], "7":["p", "q", "r", "s"], "8":["t", "u", "v"], "9":["w", "x", "y", "z"]}"o"], "7":["p", "q", "r", "s"], "8":["t", "u", "v"], "9":["w", "x", "y", "z"]}
        res = []        res = []
        def dfs(temp, i):        def dfs(temp, i):
            if i==len(digits):            if i==len(digits):
                res.append(temp)                res.append(temp)
                        
            for letter in representations[digits[i]]:            for letter in representations[digits[i]]:
                dfs(temp + letter, i + 1)                dfs(temp + letter, i + 1)
                return                return
        dfs("", 0)        dfs("", 0)
        return res        return res
                
