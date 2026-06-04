# Problem: Minimum Window Substring
# Number: 76
# Difficulty: Hard
# URL: https://leetcode.com/problems/minimum-window-substring/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: N/A

            if (need.count(s[r])) {            if (need.count(s[r])) {
                have[s[r]]++;                have[s[r]]++;
                if (have[s[r]] == need[s[r]]) {                if (have[s[r]] == need[s[r]]) {
                    current++;                    current++;
                }                }
            }            }

            while(l <= r && required == current) {            while(l <= r && required == current) {
                if (r - l + 1 < longest) {                if (r - l + 1 < longest) {
                    longest = r - l + 1;                    longest = r - l + 1;
                }                }
                if (need.count(s[l])) {                if (need.count(s[l])) {
                    if (have[s[l]] < need[s[l]]) {                    if (have[s[l]] < need[s[l]]) {
                        current--;                        current--;
                    }                    }
                }                }
                l++;                l++;
            }            }


                    bestStart = l;                    bestStart = l;
            r++;            r++;
        }        }
                    have[s[l]]--;                    have[s[l]]--;

        return s.substr(bestStart, longest);        return s.substr(bestStart, longest);
        if (bestStart == -1) {        if (bestStart == -1) {
            return "";            return "";
        }        }
    }    }
};};
