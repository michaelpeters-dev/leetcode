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
  int n;
  cin >> n;

  vector<int> a(n);
  for (int i=0; i<n; i++) {
    cin >> a[i];
  }
  
  int curSeg = 0;
  bool inSegment = false;

  for (int i = 0; i<n; i++) {
    if (a[i]!=0) {
      if (!inSegment) {
        curSeg++;
        inSegment = true;
      }
    } else {
      inSegment = false;
    }
  }

  if (curSeg==0) {
    cout << "0\n";
  } else if (curSeg==1) {
    cout << "1\n";
  } else {
    cout << "2\n";
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

