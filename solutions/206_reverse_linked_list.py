# Problem: Reverse Linked List
# Number: 206
# Difficulty: Easy
# URL: https://leetcode.com/problems/reverse-linked-list/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 0.00 MB

/**/**
 * Definition for singly-linked list. * Definition for singly-linked list.
 * struct ListNode { * struct ListNode {
 *     int val; *     int val;
 *     ListNode *next; *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {} *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {} *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {} *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * }; * };
 */ */
class Solution {class Solution {
public:public:
    ListNode* reverseList(ListNode* head) {    ListNode* reverseList(ListNode* head) {
        ListNode* prev = nullptr;        ListNode* prev = nullptr;
        ListNode* curr = head;        ListNode* curr = head;

        while (curr != nullptr) {        while (curr != nullptr) {
            ListNode* next = curr->next;            ListNode* next = curr->next;
        }        }
            curr->next = prev;            curr->next = prev;

    }    }
            curr = next;            curr = next;
            prev = curr;            prev = curr;

        return prev;        return prev;
};};
