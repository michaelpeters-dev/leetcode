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
  string a;
  string b;
  cin >> a >> b;

  int aptr = a.length() - 1;
  int bptr = b.length() - 1;

  while (bptr>=0 && aptr>=0) {
    if (b[bptr] == a[aptr]) {
      bptr--;
      aptr--;
    } else {
      aptr -= 2;
    }
  }

  if (bptr==-1) {
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

