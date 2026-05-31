# Problem: Valid Sudoku
# Number: 36
# Difficulty: Medium
# URL: https://leetcode.com/problems/valid-sudoku/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 0.00 MB

                    continue;                    continue;
                }                }

                pair<int, int> box = {row/3, col/3};                pair<int, int> box = {row/3, col/3};
                if (number == '.') {                if (number == '.') {


                char number = board[row][col];                char number = board[row][col];
                if (rows[row].count(number) || cols[col].count(number) || boxes[box].count(number)) {                if (rows[row].count(number) || cols[col].count(number) || boxes[box].count(number)) {
                    return false;                    return false;
                }                }

                rows[row].insert(number);                rows[row].insert(number);
                cols[col].insert(number);                cols[col].insert(number);
                boxes[box].insert(number);                boxes[box].insert(number);
            }            }
        }        }

