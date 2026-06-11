# Problem: Largest Rectangle in Histogram
# Number: 84
# Difficulty: Hard
# URL: https://leetcode.com/problems/largest-rectangle-in-histogram/
# Submission Status: Accepted
# Runtime: 23 ms
# Memory: 81.35 MB


            while (!st.empty() && heights[st.top()] > heights[idx]) {            while (!st.empty() && heights[st.top()] > heights[idx]) {
                int height = heights[st.top()]; st.pop();                int height = heights[st.top()]; st.pop();

                int width;                int width;
                if (st.empty()) {                if (st.empty()) {
                    width = idx;                    width = idx;
                } else {                } else {
                    width = idx - st.top() - 1;                    width = idx - st.top() - 1;
                }                }

                maxArea = max(maxArea, height * width);                maxArea = max(maxArea, height * width);
            }            }

            st.push(idx);            st.push(idx);
        }        }

        int idx = heights.size();        int idx = heights.size();
        while (!st.empty()) {        while (!st.empty()) {
            int height = heights[st.top()]; st.pop();            int height = heights[st.top()]; st.pop();
            int width;            int width;
            if (st.empty()) width = idx;            if (st.empty()) width = idx;
            else width = idx - st.top() - 1;            else width = idx - st.top() - 1;

            maxArea = max(maxArea, height * width);            maxArea = max(maxArea, height * width);
        }        }

