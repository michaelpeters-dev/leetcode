# Problem: Daily Temperatures
# Number: 739
# Difficulty: Medium
# URL: https://leetcode.com/problems/daily-temperatures/
# Submission Status: Accepted
# Runtime: 28 ms
# Memory: 107.36 MB

        // Specifically the decreasing property!        // Specifically the decreasing property!

        stack<int> st;        stack<int> st;
        // 75 72        // 75 72
        for (int i = 0; i < temperatures.size(); i++) {        for (int i = 0; i < temperatures.size(); i++) {
            if (st.size() == 0 || temperatures[st.top()] > temperatures[i]) {            if (st.size() == 0 || temperatures[st.top()] > temperatures[i]) {
                st.push(i);                st.push(i);
            }            }
        }        }
                continue;                continue;

            while (!st.empty() && temperatures[st.top()] < temperatures[i]) {            while (!st.empty() && temperatures[st.top()] < temperatures[i]) {

        vector<int> result(temperatures.size());         vector<int> result(temperatures.size()); 
                int index = st.top(); st.pop();                int index = st.top(); st.pop();
                result[index] = i - index;                result[index] = i - index;
            }            }
            st.push(i);            st.push(i);

        // Note: We need to keep the monotonic property of the stack intact        // Note: We need to keep the monotonic property of the stack intact
    vector<int> dailyTemperatures(vector<int>& temperatures) {    vector<int> dailyTemperatures(vector<int>& temperatures) {
        return result;        return result;
    }    }
};};
