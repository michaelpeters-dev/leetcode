#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using ld = long double;

#define all(x) (x).begin(), (x).end()
#define sz(x) (int)(x).size()

void fastio() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
}

#ifdef LOCAL
#else
#define dbg(x)
#endif

void solve() {
  int n;
  cin >> n;
  vector<int> a(n);


  for (int i = 0; i < n; i++) {
    cin >> a[i];
  }

  if (n == 1) {
    cout << "0\n";
    return;
  }

  int operations = 0;
  for (int i = n-1; i > 0; i--) {
    if (a[i]==0) {
        cout << "-1\n";
        return;
    }
    while (a[i] <= a[i - 1]) {
      operations++;
      a[i - 1] = a[i-1]/2;
    }
  }

 cout << operations << "\n";
}

int main() {
    fastio();

    int t = 1;
    cin >> t;   // remove this line if single test case
    while (t--) {
        solve();
    }

    return 0;
}

