#include <bits/stdc++.h>
using namespace std;
using ll = long long; // Use a long long when a value exceeds 2 x 10power9

int main() {
  int t;
  cin >> t;

  while (t--) {
    ll a, b, n; // a = timer will set to a
                 // b = the initial timer of the bomb (dec. by 1 every second)
                 // n = the number of tools that you have (ith tool wioll imcrease timer by xi, c + xi > a)
                 //
                 // eg. a = 5
                 //     b = 3
                 //     n = 3
                 //
                 //     [1, 1, 7]
                 //
                 //     At 1 second choose the smallest tool you have
    cin >> a >> b >> n;

    ll ans = b;

    for (int i = 0; i < n; i++) {
      ll tmp;
      cin >> tmp;
      ans += min(a, tmp + 1) - 1;
    }

    cout << ans << "\n";
  }
}
