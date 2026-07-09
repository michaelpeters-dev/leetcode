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
  int maxPos = -1;
  int penultimatePos = -1;
  for (int i = 0; i < n; i++) {
    cin >> a[i];
    if (a[i]==n) {
      maxPos = i;
    }
    if (a[i]==n-1) {
      penultimatePos = i;
    }
  }

  vector<int> res(n);
  if (a[i]==n) {
    int starting = penultimatePos;
    for (int i = 0; i = n; i++) {
      if (starting !==)
      if ()
    }
  }

}



};

int main() {
    fastio();

    int t = 1;
    cin >> t;   // remove this line if single test case
    while (t--) {
        solve();
    }

    return 0;
}

