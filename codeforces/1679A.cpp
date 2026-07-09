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
    long long n;
    cin >> n;

    if (n%2==1 || n<4) {
      cout << "-1\n";
      return;
    }

    long long minimum = (n + 5) / 6; // 32: 6
    long long maximum = n / 4;

    cout << minimum << " " << maximum << "\n";
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


// Notes!
//
// Let x be the bus with 4 wheels
// Let y be the buss with 6 wheels
// 4x + 6y = n
// we need to minimize and maximize x and y
//
// Minimum will be the most 6 wheels that we can fit in! 
//
