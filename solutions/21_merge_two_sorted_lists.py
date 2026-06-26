# Problem: Merge Two Sorted Lists
# Number: 21
# Difficulty: Easy
# URL: https://leetcode.com/problems/merge-two-sorted-lists/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 0.00 MB


        while (first != nullptr && second != nullptr) {        while (first != nullptr && second != nullptr) {
        }        }
            } else {            } else {
            if (first->val < second->val) {            if (first->val < second->val) {
                temp->next = first;                temp->next = first;
                temp->next = second;                temp->next = second;
            }            }
            temp = temp->next;            temp = temp->next;
                first = first->next;                first = first->next;
                second = second->next;                second = second->next;

        while (first != nullptr) {        while (first != nullptr) {
            temp->next = first;            temp->next = first;
        }        }
            first = first->next;            first = first->next;
        while (second != nullptr) {        while (second != nullptr) {
            temp->next = second;            temp->next = second;
            second = second ->next;            second = second ->next;
        ListNode* temp = &dummy;        ListNode* temp = &dummy;
        ListNode dummy(0);        ListNode dummy(0);

        ListNode* second = list2;        ListNode* second = list2;
        ListNode* first = list1;        ListNode* first = list1;
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
            temp = temp->next;            temp = temp->next;
            temp = temp->next;            temp = temp->next;
        }        }
