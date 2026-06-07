# Problem: Generate Parentheses
# Number: 22
# Difficulty: Medium
# URL: https://leetcode.com/problems/generate-parentheses/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 0.00 MB

class Solution {class Solution {
public:public:
    void dfs(int open, int closed, int n, string current, vector<string>& result) {    void dfs(int open, int closed, int n, string current, vector<string>& result) {
        if (current.size() == 2*n) {        if (current.size() == 2*n) {
            result.push_back(current);            result.push_back(current);
            return;            return;
        }        }

        if (open < n) {        if (open < n) {
            dfs(open + 1, closed, n, current + "(", result);            dfs(open + 1, closed, n, current + "(", result);
        }        }

        if (closed < open) {        if (closed < open) {
            dfs(open, closed + 1, n, current + ")", result);            dfs(open, closed + 1, n, current + ")", result);
        }        }
    }    }
    vector<string> generateParenthesis(int n) {    vector<string> generateParenthesis(int n) {

        vector<string> result;        vector<string> result;
    }    }
        dfs(0, 0, n, "", result);        dfs(0, 0, n, "", result);
        return result;        return result;
};};
