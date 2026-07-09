#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using ld = long double;

#define all(x) (x).begin(), (x).end()
#define sz(x) (int)(x).size()

// Fast I/O
void fastio() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
}

// Optional debug (comment out in contest if needed)
#ifdef LOCAL
#define dbg(x) cerr << #x << " = " << x << '\n';
#else
#define dbg(x)
#endif

void solve() {
  // We can either rotate the entire array,
  // or we can move the min to the start (leaving the last the same)
  // or we can move the max to the end (leaving the min the same)

  int n;
  cin >> n;


  int maxAfterOne = INT_MIN;
  int minBeforeLast = INT_MAX;

  vector<int> a(n);
  for (int i = 0; i < n; i++) {
    cin >> a[i];
    if (i>=1) {
      maxAfterOne = max(maxAfterOne, a[i]);
    }
    if (i<n-1) {
      minBeforeLast = min(minBeforeLast, a[i]);
    }
  }

  int maximum = a[n - 1] - a[0];
  maximum = max(maximum, a[n-1] - minBeforeLast);
  maximum = max(maximum, maxAfterOne - a[0]);

  int l = 0;
  int r = n - 1;
  for (int i = 0; i < n; i++) { // 1 3 9 11 5 7 THEN 7 1 3 9 1
    r = (r - 1 + n)%n;
    l = (l - 1 + n)%n;
    maximum = max(maximum, a[r] - a[l]);
  }

  if (n==1) {
    maximum = 0;
  }
  cout << maximum << "\n";
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

