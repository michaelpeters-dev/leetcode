# Problem: Time Based Key-Value Store
# Number: 981
# Difficulty: Medium
# URL: https://leetcode.com/problems/time-based-key-value-store/
# Submission Status: Accepted
# Runtime: 68 ms
# Memory: 136.48 MB

        int l = 0;        int l = 0;
        }        }
        int r = mp[key].size();        int r = mp[key].size();

        while (l < r) {        while (l < r) {
        }        }
            int mid = (l + r) / 2;            int mid = (l + r) / 2;
            int value = mp[key][mid].first;            int value = mp[key][mid].first;

            if (value <= timestamp) {            if (value <= timestamp) {
            return "";             return ""; 
            } else {            } else {
            }            }
                l = mid + 1;                l = mid + 1;
                r = mid;                r = mid;

        if (mp.count(key) == 0) {        if (mp.count(key) == 0) {
    string get(string key, int timestamp) {    string get(string key, int timestamp) {
        
    }    }
        mp[key].push_back({timestamp, value});        mp[key].push_back({timestamp, value});
    void set(string key, string value, int timestamp) {    void set(string key, string value, int timestamp) {

        return mp[key][l - 1].second;        return mp[key][l - 1].second;
        if (l == 0) return "";        if (l == 0) return "";
    }    }
