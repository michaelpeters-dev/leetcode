# Problem: Last Stone Weight
# Number: 1046
# Difficulty: Easy
# URL: https://leetcode.com/problems/last-stone-weight/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 10.06 MB

        }        }
            pq.pop();            pq.pop();

            if (x == y) {            if (x == y) {
                continue;                continue;
            } else if (x != y) {            } else if (x != y) {
                pq.push(abs(y - x));                pq.push(abs(y - x));
            }            }

        if (pq.size() == 0) {        if (pq.size() == 0) {
            return 0;            return 0;
        } else {        } else {
            return pq.top();            return pq.top();
        }        }
    }    }
};};
            int y = pq.top();            int y = pq.top();

            pq.pop();            pq.pop();
            int x = pq.top();            int x = pq.top();
