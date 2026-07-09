#include <bits/stdc++.h>
using namespace std;

int main() {
  int t;
  cin >> t;
  while (t--) {
    int n, k;
    cin >> n >> k;
    map<char, int> letters; // If n is even: we can need to have an even number of odd letters, and if n is odd we need to have an odd number of odd letters
                            // Therefore if even, (odd letters - k >=) must be even, if n is odd (odd letters - k) must be odd
                            // oddCount-k%2=0 for even length ones and oddCount-k%2==1 for odd length strings
    for (int i = 0; i < n; i++) {
      char letter;
      cin >> letter;
      letters[letter] += 1;
    }

    int oddCount = 0;
    for (auto x: letters) {
      if (x.second%2==1) {
        oddCount++;
      }
    }
    
    if (oddCount - 1 <= k) { // odd - k <= 1, odd - 1 <= k
      cout << "YES\n";
    } else {
      cout << "NO\n";
    }
  }
}
