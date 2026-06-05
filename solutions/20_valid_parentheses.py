# Problem: Valid Parentheses
# Number: 20
# Difficulty: Easy
# URL: https://leetcode.com/problems/valid-parentheses/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 0.00 MB

        };        };

        for (const auto& ch: s) {        for (const auto& ch: s) {
            if (stack.size() == 0) {            if (stack.size() == 0) {
                stack.push_back(ch);                stack.push_back(ch);
            } else {            } else {
                if (stack.back() == dict[ch]) {                if (stack.back() == dict[ch]) {
            }            }
                    stack.pop_back();                    stack.pop_back();
                } else {                } else {
                    stack.push_back(ch);                    stack.push_back(ch);
                }                }
        }        }

        return stack.size() == 0;        return stack.size() == 0;
    }    }
};};
