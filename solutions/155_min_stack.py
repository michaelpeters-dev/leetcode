# Problem: Min Stack
# Number: 155
# Difficulty: Medium
# URL: https://leetcode.com/problems/min-stack/
# Submission Status: Accepted
# Runtime: 47 ms
# Memory: 152.51 MB

        
    void pop() {    void pop() {
        
    int top() {    int top() {
        stack.pop_back();        stack.pop_back();
    }    }
        return stack.back();        return stack.back();
    }    }
        
    int getMin() {    int getMin() {
        return minStack.back();        return minStack.back();
        minStack.pop_back();        minStack.pop_back();
    }    }
        }        }
        } else {        } else {
            minStack.push_back(min(minStack.back(), value));            minStack.push_back(min(minStack.back(), value));
            minStack.push_back(value);            minStack.push_back(value);
        if (stack.size() == 1) {        if (stack.size() == 1) {
        stack.push_back(value);           stack.push_back(value);   
    void push(int value) {    void push(int value) {
        
    }    }
    MinStack() {    MinStack() {
    vector<int> minStack;    vector<int> minStack;
    vector<int> stack;    vector<int> stack;
    }    }
};};
