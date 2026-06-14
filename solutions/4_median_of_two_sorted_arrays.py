# Problem: Median of Two Sorted Arrays
# Number: 4
# Difficulty: Hard
# URL: https://leetcode.com/problems/median-of-two-sorted-arrays/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 0.00 MB

        int l = 0;        int l = 0;
        int r = smaller->size();        int r = smaller->size();
        while (l <= r) {        while (l <= r) {
            int cut1 = (l + r) / 2;            int cut1 = (l + r) / 2;
            int cut2 = ((m + n + 1) / 2) - cut1; // half the t-array minus the left partition            int cut2 = ((m + n + 1) / 2) - cut1; // half the t-array minus the left partition

            int left1 = (cut1 == 0) ? INT_MIN : (*smaller)[cut1 - 1];            int left1 = (cut1 == 0) ? INT_MIN : (*smaller)[cut1 - 1];
            int right1 = (cut1 == m) ? INT_MAX : (*smaller)[cut1];            int right1 = (cut1 == m) ? INT_MAX : (*smaller)[cut1];

            int left2 = (cut2 == 0) ? INT_MIN : (*larger)[cut2 - 1];            int left2 = (cut2 == 0) ? INT_MIN : (*larger)[cut2 - 1];
            int right2 = (cut2 == n) ? INT_MAX : (*larger)[cut2];            int right2 = (cut2 == n) ? INT_MAX : (*larger)[cut2];

            if (left1 > right2) {            if (left1 > right2) {
                r = cut1 - 1;                r = cut1 - 1;
            } else if (left2 > right1) {            } else if (left2 > right1) {
                l = cut1 + 1;                l = cut1 + 1;
            } else {            } else {
                int leftSide = max(left1, left2);                int leftSide = max(left1, left2);
                if ((m + n)% 2 == 1) {                if ((m + n)% 2 == 1) {
                    return leftSide;                    return leftSide;
                }                }

                int rightSide = min(right1, right2);                int rightSide = min(right1, right2);
                return static_cast<double>(leftSide + rightSide)/2;                return static_cast<double>(leftSide + rightSide)/2;
            }            }
        }        }

        return 0;        return 0;
    }    }
};};
