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

    sort(a.begin(), a.end());

    if (a[0] == a[n - 1]) {
      cout << "NO\n";
      continue;
    }

    cout << "YES\n";

    swap(a[0], a[n - 1]);
    sort(a.begin() + 1, a.end());

    for (int x : a) {
      cout << x << " ";
    }
    cout << "\n";
  }
}
