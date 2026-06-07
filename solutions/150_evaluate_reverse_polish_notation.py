# Problem: Evaluate Reverse Polish Notation
# Number: 150
# Difficulty: Medium
# URL: https://leetcode.com/problems/evaluate-reverse-polish-notation/
# Submission Status: Accepted
# Runtime: 3 ms
# Memory: 17.08 MB

public:public:
    int evalRPN(vector<string>& tokens) {    int evalRPN(vector<string>& tokens) {
        stack<int> st;        stack<int> st;

        for (const auto& token: tokens) {        for (const auto& token: tokens) {
        }        }
            if (token == "+" || token == "-" || token == "*" || token == "/") {            if (token == "+" || token == "-" || token == "*" || token == "/") {

        return st.top();        return st.top();
                int two = st.top(); st.pop();                int two = st.top(); st.pop();
            } else {            } else {
                int one = st.top(); st.pop();                int one = st.top(); st.pop();

                if (token == "+") {                if (token == "+") {
                    st.push(one + two);                    st.push(one + two);
                } else if (token == "-") {                } else if (token == "-") {
                int temp{};                int temp{};
                    st.push(one - two);                    st.push(one - two);
                } else if (token == "*") {                } else if (token == "*") {
                    st.push(one * two);                    st.push(one * two);
                } else {                } else {
                    st.push(one / two);                    st.push(one / two);
                }                }
                st.push(stoi(token));                st.push(stoi(token));
            }            }
    }    }
};};
