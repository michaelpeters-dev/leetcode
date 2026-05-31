# Problem: Best Time to Buy and Sell Stock
# Number: 121
# Difficulty: Easy
# URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 0.00 MB

class Solution {class Solution {
public:public:
    int maxProfit(vector<int>& prices) {    int maxProfit(vector<int>& prices) {
        int minimum = INT_MAX;        int minimum = INT_MAX;

        for (const auto& price: prices) {        for (const auto& price: prices) {
        }        }
        int best = 0;        int best = 0;
            minimum = min(minimum, price);            minimum = min(minimum, price);
    }    }

        return best;        return best;
            best = max(best, price - minimum);            best = max(best, price - minimum);
};};
