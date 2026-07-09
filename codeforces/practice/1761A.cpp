#include <bits/stdc++.h>
using namespace std;

int main() {
  int t;
  cin >> t;

  while (t--) {
    int n, a, b;
    cin >> n >> a >> b;

    if (n==1) {
      cout << "Yes\n";
      continue;
    }

    if (a + b <= n - 2 || (a==n & b==n)) {
      cout << "yes\n";
    } else {
      cout << "no\n";
    }


    // n = 2: [1, 2] [1, 2] NO [2, 1] [1, 2] = 0 | 2 OR 0 >>>>>>> 1 + 1 = 2, n=2
    // n = 3: [1, 2, 3] OR [1, _ 3] | 3 OR 0 >>>>>>>>>> 1 + 1 = 2, n=3
    // n = 4: [1, 2, 3, 4] [1, 3, 2, 4] >>>>>>> 1 + 1 = 2, n=4
    // n = 5: [_ _, X, _ _] >>>>> 2 + 2 = 4, n = 5
  }
}
