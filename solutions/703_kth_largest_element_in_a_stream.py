# Problem: Kth Largest Element in a Stream
# Number: 703
# Difficulty: Easy
# URL: https://leetcode.com/problems/kth-largest-element-in-a-stream/
# Submission Status: Accepted
# Runtime: 6 ms
# Memory: 0.00 MB

class KthLargest {class KthLargest {
public:public:
    KthLargest(int k, vector<int>& nums) {    KthLargest(int k, vector<int>& nums) {
        this->k = k;        this->k = k;
    }    }
        
    int add(int val) {    int add(int val) {
        pq.push(val);        pq.push(val);
    }    }
};};

/**/**
 * Your KthLargest object will be instantiated and called as such: * Your KthLargest object will be instantiated and called as such:
    priority_queue<int, vector<int>, greater<int>> pq;    priority_queue<int, vector<int>, greater<int>> pq;
    int k;    int k;
        for (const auto& num: nums) {        for (const auto& num: nums) {
            pq.push(num);            pq.push(num);
        }        }
            if (pq.size() > k) {            if (pq.size() > k) {
                pq.pop();                pq.pop();
            }            }
        if (pq.size() > k) {        if (pq.size() > k) {
            pq.pop();            pq.pop();
        }        }
        return pq.top();        return pq.top();
 * KthLargest* obj = new KthLargest(k, nums); * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val); * int param_1 = obj->add(val);

 */ */
