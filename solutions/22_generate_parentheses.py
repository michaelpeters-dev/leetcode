# Problem: Generate Parentheses
# Number: 22
# Difficulty: Medium
# URL: https://leetcode.com/problems/generate-parentheses/
# Submission Status: Accepted
# Runtime: 134 ms
# Memory: 18.23 MB

        def dfs(i, temp):        def dfs(i, temp):
        res = []        res = []
            if i==(n*2):            if i==(n*2):
                if validParenthesis(temp):                if validParenthesis(temp):
                    res.append(temp)                    res.append(temp)

            return True if len(stack)==0 else False            return True if len(stack)==0 else False
                stack.append(letter)                stack.append(letter)
            for i, letter in enumerate(string):            for i, letter in enumerate(string):
            stack = []            stack = []
        def validParenthesis(string):        def validParenthesis(string):
    def generateParenthesis(self, n: int) -> List[str]:    def generateParenthesis(self, n: int) -> List[str]:
class Solution:class Solution:
                if len(stack)>1 and stack[-1]==")" and stack[-2]=="(":                if len(stack)>1 and stack[-1]==")" and stack[-2]=="(":
                    stack.pop()                    stack.pop()
                    stack.pop()                    stack.pop()
                return                return
                        
