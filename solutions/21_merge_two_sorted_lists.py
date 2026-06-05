# Problem: Merge Two Sorted Lists
# Number: 21
# Difficulty: Easy
# URL: https://leetcode.com/problems/merge-two-sorted-lists/
# Submission Status: Accepted
# Runtime: 2 ms
# Memory: 19.53 MB

        }        }
            } else {            } else {
            }            }
                tail->next = list2;                tail->next = list2;
                list2 = list2->next;                list2 = list2->next;

            tail = tail->next;            tail = tail->next;

        if (list1 == nullptr) {        if (list1 == nullptr) {
                list1 = list1->next;                list1 = list1->next;
                tail->next = list1;                tail->next = list1;

        while (list1 != nullptr && list2 != nullptr) {        while (list1 != nullptr && list2 != nullptr) {
            if (list1->val <= list2->val) {            if (list1->val <= list2->val) {
        ListNode* tail = &dummy;        ListNode* tail = &dummy;
            while (list2 != nullptr) {            while (list2 != nullptr) {
                tail->next = list2;                tail->next = list2;
                tail = tail->next;                tail = tail->next;
                list2 = list2->next;                list2 = list2->next;
            }            }
        } else {        } else {
            while (list1 != nullptr) {            while (list1 != nullptr) {
                tail->next = list1;                tail->next = list1;
                tail = tail->next;                tail = tail->next;
                list1 = list1->next;                list1 = list1->next;
        ListNode dummy;        ListNode dummy;
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
public:public:
class Solution {class Solution {
 */ */
