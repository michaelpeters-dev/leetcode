# Problem: Sliding Window Maximum
# Number: 239
# Difficulty: Hard
# URL: https://leetcode.com/problems/sliding-window-maximum/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 0.00 MB

        vector<int> result;        vector<int> result;
        deque<int> dq;        deque<int> dq;

        for (int i = 0; i < nums.size(); i++) {        for (int i = 0; i < nums.size(); i++) {
            while (!dq.empty() && dq.front() <= i - k) {            while (!dq.empty() && dq.front() <= i - k) {
                dq.pop_front();                dq.pop_front();
            }            }

            while (!dq.empty() && nums[dq.back()] < nums[i]) {            while (!dq.empty() && nums[dq.back()] < nums[i]) {
                dq.pop_back();                dq.pop_back();
            }            }

            dq.push_back(i);            dq.push_back(i);

            if (i >= k - 1) {            if (i >= k - 1) {
                result.push_back(nums[dq.front()]);                result.push_back(nums[dq.front()]);
            }            }
        }        }

        return result;        return result;
    }    }
};};
