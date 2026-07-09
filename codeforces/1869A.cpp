#include <bits/stdc++.h>
using namespace std;

int main() {
  int t;
  cin >> t;
  while (t--) {
    int n;
    cin >> n;
    vector<int> a(n);

    for (int i = 0; i < n; i++) {
      cin >> a[i];
    }

    // For even n, apply XOR to the entire array twice
    // For odd n, apply XOR to (1-n-1 twice) apply xor to n-1, n twice
    if (n%2==0) {
      cout << "2\n";
      cout << 1 << " " << n << "\n";
      cout << 1 << " " << n << "\n";
    } else {
      cout << "4\n";
      cout << 1 << " " << n-1 << "\n";
      cout << 1 << " " << n-1 << "\n";
      cout << n-1 << " " << n << "\n";
      cout << n-1 << " " << n << "\n";
    }

  }
}
