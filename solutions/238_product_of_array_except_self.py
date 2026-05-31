# Problem: Product of Array Except Self
# Number: 238
# Difficulty: Medium
# URL: https://leetcode.com/problems/product-of-array-except-self/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 40.12 MB

        int suffix = 1;        int suffix = 1;

        for (int i = nums.size() - 1; i>=0; i--) {        for (int i = nums.size() - 1; i>=0; i--) {
            answer[i] *= suffix;            answer[i] *= suffix;
            suffix *= nums[i];            suffix *= nums[i];
        }        }
        return answer;        return answer;
    }    }

        }        }
            prefix *= nums[i];            prefix *= nums[i];
            answer[i] *= prefix;            answer[i] *= prefix;
        for (int i = 0; i < nums.size(); i++) {        for (int i = 0; i < nums.size(); i++) {
};};
