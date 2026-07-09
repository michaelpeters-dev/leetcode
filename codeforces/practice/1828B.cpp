#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
  int t;
  cin >> t;
  while (t--) {
    int n;
    cin >> n;

    int g = 0;
    for (int i = 1; i < n + 1; i++) {
      int x;
      cin >> x;

      g = gcd(g, abs(x - i));
    }

    cout << g << "\n";
  }
}
