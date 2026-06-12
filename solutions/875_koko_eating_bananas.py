# Problem: Koko Eating Bananas
# Number: 875
# Difficulty: Medium
# URL: https://leetcode.com/problems/koko-eating-bananas/
# Submission Status: Accepted
# Runtime: 21 ms
# Memory: 22.98 MB

        int l = 1; // We look at values, not indices in the array        int l = 1; // We look at values, not indices in the array
        int r = *max_element(piles.begin(), piles.end());        int r = *max_element(piles.begin(), piles.end());

        while (l < r) {        while (l < r) {
            k = (l + r) / 2;            k = (l + r) / 2;
        }        }
            int hours = 0;            int hours = 0;

            for (const auto& pile: piles) {            for (const auto& pile: piles) {
                hours += ceil(double(pile) / k);                hours += ceil(double(pile) / k);

            if (hours > h) {            if (hours > h) {
                l = k + 1;                l = k + 1;
            } else if (hours <= h) {            } else if (hours <= h) {
                r = k;                r = k;
            }            }
    }    }
        int k{};        int k{};

        return l;        return l;
    int minEatingSpeed(vector<int>& piles, int h) {    int minEatingSpeed(vector<int>& piles, int h) {
public:public:
class Solution {class Solution {
            }            }
};};
