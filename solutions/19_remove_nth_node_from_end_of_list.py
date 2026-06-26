# Problem: Remove Nth Node From End of List
# Number: 19
# Difficulty: Medium
# URL: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 0.00 MB

 * }; * };
 */ */
class Solution {class Solution {
public:public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* fast = &dummy;        ListNode* fast = &dummy;

        for (int i = 0; i < n; i++) {        for (int i = 0; i < n; i++) {
        }        }
            fast = fast->next;            fast = fast->next;

        while (fast->next != nullptr) {        while (fast->next != nullptr) {
            slow = slow->next;            slow = slow->next;
        }        }
            fast = fast->next;            fast = fast->next;

        slow->next = slow->next->next;        slow->next = slow->next->next;

    }    }
        ListNode* slow = &dummy;        ListNode* slow = &dummy;
        return dummy.next;        return dummy.next;
        ListNode dummy(0, head);        ListNode dummy(0, head);

};};
