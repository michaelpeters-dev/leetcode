#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
  int t;
  cin >> t;

  while (t--) {
    // we get three integers n, k and x;
    // we need to find k1 , ..., kp < n such that k1 + ... + kp = x
    // take the k smallest numbers: 1, 2, 3, ..., k
    //
    // min_sum = 1 + 2 + ... + k
    // formula: min_sum = k(k + 1)/2
    //
    // max_sum = n, n - 1, n - 2, ..., n - k + 1:          sum = k(a + l)/2, this is the formula for an arithmetic sequence (k=num terms, a=first-term, l=last-term)
    // formula: max_sum = (n)(n + n - k + 1)/2 = k(2n - k + 1)/2
    //
    // therefore, all we need to do is check if x lies within these two bounds, as this would be the max and min sum that we can compute
    
    ll n, k, x;
    cin >> n >> k >> x;

    ll min_sum = k * (k + 1)/2;
    ll max_sum = k * (2*n - k + 1)/2;

    if (min_sum<=x and max_sum>=x) {
      cout << "yes\n";
    } else {
      cout << "no\n";
    }

  }
};
