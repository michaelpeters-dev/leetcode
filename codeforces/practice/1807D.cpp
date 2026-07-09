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
  int n, q;
  cin >> n >> q;

  int oddCount = 0;
  vector<int> a(n + 1);
  for (int i = 1; i < n + 1; i++) { 
    int num;
    cin >> num;
    a[i] = a[i - 1] + num%2;
    if (num%2==1) {
      oddCount++;
    }
  }

  while (q--) {
    int start, stop, change;
    cin >> start >> stop >> change;


    int odds = a[start - 1] + (a[n] - a[stop]);

     if (change%2==1) {
       odds += stop - start + 1;
     } else {
       ;
     }
    
    cout << ((odds)%2==1 ? "YES" : "NO") << "\n";
  }

}

int main() {
    fastio();

    int t;
    cin >> t;
    while (t--) {
        solve();
    }

    return 0;
}

