#include <bits/stdc++.h>
#include <cmath>
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
  int k;
  cin >> n >> k;

  string s;
  cin >> s;
  int ones = 0;
  int zeros = 0;
  for (char temp: s) {
    if (temp == '0') {
      zeros++;
    } else {
      ones++;
    }
  }

  if (k > n/2) {
    cout << "NO\n";
    return;
  }

  int maximum = ones/2 + zeros/2;
  int minimum = n/2 - min(zeros, ones);

  if (maximum >= k && k >= minimum && (maximum - k)%2==0) {
    cout << "YES\n";
  } else {
    cout << "NO\n";
  }
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

