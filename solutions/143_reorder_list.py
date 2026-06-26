# Problem: Reorder List
# Number: 143
# Difficulty: Medium
# URL: https://leetcode.com/problems/reorder-list/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 0.00 MB

        ListNode* second = slow->next;        ListNode* second = slow->next;
        slow->next = nullptr;        slow->next = nullptr;

        ListNode* prev = nullptr;        ListNode* prev = nullptr;
        while (second != nullptr) {        while (second != nullptr) {
            ListNode* next = second->next;            ListNode* next = second->next;

            second->next = prev;            second->next = prev;
            prev = second;            prev = second;
            second = next;            second = next;
        }        }

        }        }
            fast = fast->next->next;            fast = fast->next->next;
            slow = slow->next;            slow = slow->next;
        while (fast->next != nullptr && fast->next->next != nullptr) {        while (fast->next != nullptr && fast->next->next != nullptr) {

        ListNode* fast = head;        ListNode* fast = head;
        ListNode* slow = head;        ListNode* slow = head;
        }        }

    void reorderList(ListNode* head) {    void reorderList(ListNode* head) {
        if (head == nullptr || head->next == nullptr) {        if (head == nullptr || head->next == nullptr) {
            return;            return;
class Solution {class Solution {
public:public:
 */ */
 * }; * };
 *     ListNode(int x, ListNode *next) : val(x), next(next) {} *     ListNode(int x, ListNode *next) : val(x), next(next) {}
