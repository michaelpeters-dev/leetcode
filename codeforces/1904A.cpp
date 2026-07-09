#include <bits/stdc++.h>
using namespace std;

int main() {
  int t;
  cin >> t;
  while (t--) {

    long long a, b;
    cin >> a >> b;

    long long xK, yK, xQ, yQ;
    cin >> xK >> yK >> xQ >> yQ;

    set<pair<long, long>> SK;
    set<pair<long, long>> SQ;

    vector<pair<long long, long long>> moves = {
      {a, b},
      {a, -b},
      {-a, b},
      {-a, -b},
      {b, a},
      {b, -a},
      {-b, a},
      {-b, -a},
    };

    for (auto [newA, newB]: moves) {
      pair<long, long> newK = {xK + newA, yK + newB};
      pair<long, long> newQ = {xQ + newA, yQ + newB};

      SK.insert(newK);
      SQ.insert(newQ);
    }

    int ans = 0;
    for (pair<long,long> x: SK) {
      if (SQ.count(x)) {
        ans ++;
      }
    }

    cout << ans << "\n";
  }
}
