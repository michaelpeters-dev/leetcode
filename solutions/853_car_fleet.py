# Problem: Car Fleet
# Number: 853
# Difficulty: Medium
# URL: https://leetcode.com/problems/car-fleet/
# Submission Status: Accepted
# Runtime: 94 ms
# Memory: 105.82 MB

        vector<pair<int, double>> cars(position.size()); // Storing (position, time_to_target)        vector<pair<int, double>> cars(position.size()); // Storing (position, time_to_target)

        for (int i = 0; i < position.size(); i++) {        for (int i = 0; i < position.size(); i++) {
            cars[i].first = position[i]; // Storing position            cars[i].first = position[i]; // Storing position
            cars[i].second = (double)(target - position[i]) / speed[i];            cars[i].second = (double)(target - position[i]) / speed[i];
        }        }


        sort(cars.rbegin(), cars.rend());        sort(cars.rbegin(), cars.rend());
        int fleets{};        int fleets{};
        double prevFleet = INT_MIN;        double prevFleet = INT_MIN;
    }    }

        for (const auto& car: cars) {        for (const auto& car: cars) {
        }        }
            if (car.second > prevFleet) {            if (car.second > prevFleet) {
            } else {            } else {
                fleets++;                fleets++;
                prevFleet = car.second;                   prevFleet = car.second;   
                continue;                continue;
            }            }

        return fleets;        return fleets;
};};
    int carFleet(int target, vector<int>& position, vector<int>& speed) {    int carFleet(int target, vector<int>& position, vector<int>& speed) {
public:public:
class Solution {class Solution {
