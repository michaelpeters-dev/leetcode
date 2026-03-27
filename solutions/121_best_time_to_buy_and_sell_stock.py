# Problem: Best Time to Buy and Sell Stock
# Number: 121
# Difficulty: Easy
# URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 97.22 MB

class Solution {class Solution {
public:public:
    int maxProfit(vector<int>& prices) {    int maxProfit(vector<int>& prices) {
        int result = 0;        int result = 0;
        int minimum = INT_MAX;        int minimum = INT_MAX;
        for (auto price: prices) {        for (auto price: prices) {
            if (price < minimum) {            if (price < minimum) {

                minimum = price;                minimum = price;
            } else if (price > minimum){            } else if (price > minimum){
                continue;                continue;
        }        }
                result = max(price - minimum, result);                result = max(price - minimum, result);
            }            }
    }    }
        return result;        return result;
};};
