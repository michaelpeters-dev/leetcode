# Problem: Copy List with Random Pointer
# Number: 138
# Difficulty: Medium
# URL: https://leetcode.com/problems/copy-list-with-random-pointer/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 0.00 MB


        if (head == nullptr) {        if (head == nullptr) {
            return nullptr;            return nullptr;
        }        }

        Node* curr = head;        Node* curr = head;

        while (curr != nullptr) {        while (curr != nullptr) {
            copies[curr] = new Node(curr->val);            copies[curr] = new Node(curr->val);
            curr = curr->next;            curr = curr->next;
        }        }

        curr = head;        curr = head;

        while (curr != nullptr) {        while (curr != nullptr) {
            copies[curr]->next = copies[curr->next];            copies[curr]->next = copies[curr->next];
        }        }
    }    }
            copies[curr]->random = copies[curr->random];            copies[curr]->random = copies[curr->random];

            curr = curr->next;            curr = curr->next;

        return copies[head];        return copies[head];
};};
