# Problem: Kth Largest Element in a Stream
# Number: 703
# Difficulty: Easy
# URL: https://leetcode.com/problems/kth-largest-element-in-a-stream/
# Submission Status: Accepted
# Runtime: 17 ms
# Memory: 33.08 MB

class KthLargest {class KthLargest {
public:public:
    }    }
        this->k = k;            this->k = k;    
    KthLargest(int k, vector<int>& nums) {    KthLargest(int k, vector<int>& nums) {
        
    int add(int val) {    int add(int val) {
    }    }
        pq.push(val);        pq.push(val);
};};

/**/**
 * Your KthLargest object will be instantiated and called as such: * Your KthLargest object will be instantiated and called as such:
    int k;    int k;
    priority_queue<int, vector<int>, greater<int>> pq;    priority_queue<int, vector<int>, greater<int>> pq;


        for (int num: nums) {        for (int num: nums) {
            pq.push(num);            pq.push(num);
        }        }

            if (pq.size() > k) {            if (pq.size() > k) {
                pq.pop();                pq.pop();
            }            }
        if (pq.size() > k) {        if (pq.size() > k) {
            pq.pop();            pq.pop();
        }        }

        return pq.top();        return pq.top();
