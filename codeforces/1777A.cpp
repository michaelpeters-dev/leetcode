#include <bits/stdc++.h>
using namespace std;

int main() {
  int t;
  cin >> t;
  while (t--) {
    int n;
    cin >> n;
    vector<int> a;

    int operations = 0;
    int previous;
    cin >> previous;
    for (int i = 0; i<n-1; i++) {
      int temp;
      cin >> temp;
      if (previous%2==temp%2) {
        operations++;
      }
      previous = temp;
    }

    cout << operations << "\n";
  }
}
