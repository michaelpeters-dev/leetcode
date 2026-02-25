# Problem: Best Time to Buy and Sell Stock
# Number: 121
# Difficulty: Easy
# URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 97.42 MB

        for (auto price: prices) {        for (auto price: prices) {
            if (price<minimum) {            if (price<minimum) {
                minimum = price;                minimum = price;
            }            }
                maximum = price;                maximum = price;
                continue;                continue;
            if (price>maximum) {            if (price>maximum) {
                maximum = price;                maximum = price;
                ans = max(ans, maximum - minimum);                ans = max(ans, maximum - minimum);
            }            }
        }        }
        return ans;        return ans;
    }    }
};};
