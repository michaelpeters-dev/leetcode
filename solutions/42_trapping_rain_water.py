# Problem: Trapping Rain Water
# Number: 42
# Difficulty: Hard
# URL: https://leetcode.com/problems/trapping-rain-water/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: N/A

            return 0;            return 0;
        }        }

        int l = 0;        int l = 0;
        int r = n - 1;        int r = n - 1;

        while (l < r) {        while (l < r) {
        int sum = 0;        int sum = 0;
            leftMax = max(leftMax, height[l]);            leftMax = max(leftMax, height[l]);
        int leftMax = 0;        int leftMax = 0;
        int rightMax = 0;        int rightMax = 0;
            rightMax = max(rightMax, height[r]);            rightMax = max(rightMax, height[r]);

            if (leftMax < rightMax) {            if (leftMax < rightMax) {
                sum += leftMax - height[l];                sum += leftMax - height[l];
                l++;                l++;
            } else {            } else {
                sum += rightMax - height[r];                sum += rightMax - height[r];
                r--;                r--;
            }            }
        }        }
            cout << sum << endl;            cout << sum << endl;
        return sum;        return sum;
    }    }
