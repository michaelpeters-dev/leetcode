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

  vector<ll> a(n);
  for (auto &x: a) {
    cin >> x;
  }

  if (a[0] == 1) {
    a[0]++;
  }

  for (int i = 1; i < n; i++) {
    if (a[i] == 1) {
      a[i] ++;
    }
    if (a[i] % a[i - 1] == 0) {
      a[i] ++;
    }
  }

  for (auto x: a) {
    cout << x << " ";
  }

  cout << "\n";

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

