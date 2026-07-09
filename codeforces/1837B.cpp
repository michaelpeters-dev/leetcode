#include <bits/stdc++.h>
using namespace std;
using ll = long long ;

int main() {
  int t;
  cin >> t;
  while (t--) {
      // < < > > [13 < 37 < 42 > 37 > 13] -> 3
      int n;
      cin >> n;
      string s;
      cin >> s;
    
      int curr = 1;
      int best = 1;
      for (int i = 1; i < n; i++) {
        if (s[i]==s[i-1]) {
          curr++;
          best = max(best, curr);
        } else {
          curr = 1;
        }
      }

      cout << best + 1<< "\n";
  }
}
