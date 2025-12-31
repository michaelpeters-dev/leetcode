# Problem: Evaluate Reverse Polish Notation
# Number: 150
# Difficulty: Medium
# URL: https://leetcode.com/problems/evaluate-reverse-polish-notation/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: N/A

class Solution:class Solution:
    def evalRPN(self, tokens: List[str]) -> int:    def evalRPN(self, tokens: List[str]) -> int:
        stack = []        stack = []
        for i in range(len(tokens)):        for i in range(len(tokens)):
            if tokens[i] in "+-/*":            if tokens[i] in "+-/*":
                operation = tokens[i]                operation = tokens[i]
            else:            else:
                stack.append(int(tokens[i]))                stack.append(int(tokens[i]))
                second_operand = stack.pop()                second_operand = stack.pop()
                first_operand = stack.pop()                first_operand = stack.pop()
                if operation=="+": stack.append(first_operand + second_operand)                if operation=="+": stack.append(first_operand + second_operand)
                elif operation=="-": stack.append(first_operand - second_operand)                elif operation=="-": stack.append(first_operand - second_operand)
                elif operation=="*": stack.append(first_operand * second_operand)                elif operation=="*": stack.append(first_operand * second_operand)
                elif operation=="/": stack.append(int(first_operand / second_operand))                elif operation=="/": stack.append(int(first_operand / second_operand))
        return stack[0]        return stack[0]
                                
