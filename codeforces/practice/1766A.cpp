#include <bits/stdc++.h>
using namespace std;

int main() {
  int t;
  cin >> t;

  while (t--) {
    int n;
    cin >> n;

    int previous = 0;
    int power = 0;
    while(n) {
      power++;
      previous = n%10;
      n = n/10;
    }


    cout << (9*(power-1)) + (previous) << "\n";
  }
}
