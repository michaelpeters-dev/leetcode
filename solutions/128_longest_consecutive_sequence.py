# Problem: Longest Consecutive Sequence
# Number: 128
# Difficulty: Medium
# URL: https://leetcode.com/problems/longest-consecutive-sequence/
# Submission Status: Accepted
# Runtime: 79 ms
# Memory: 88.90 MB

        }        }

        int longest = 0;        int longest = 0;
        for (const auto& num: store) {        for (const auto& num: store) {
            if (!store.count(num - 1)) {            if (!store.count(num - 1)) {
                int temp = num;                int temp = num;
                int counter = 1;                int counter = 1;
                while(store.count(temp)) {                while(store.count(temp)) {
                    longest = max(longest, counter);                    longest = max(longest, counter);
                    temp++;                    temp++;
                    counter++;                    counter++;
                }                }
            }            }
        }        }

        return longest;        return longest;
    }    }
