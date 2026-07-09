#include <bits/stdc++.h>
using namespace std;

int main() {
  int t;
  cin >> t;

  vector<vector<int>> board;

  while (t--) {
    for (int i = 0; i < 8;) {
      for (int j = 0; i < 8; i++) {
        string temp;
        cin >> temp;
        board[i][j] = temp;
      }
    }
  }
}
