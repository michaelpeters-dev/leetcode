#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        long long a, b, c, d;
        cin >> a >> b >> c >> d;
        if (b>d || c > a + (d-b)) {
            cout << "-1\n";
        } else {
            long long temp = (d - b) + (a + (d - b) - c);
            cout << temp << "\n";
        }
    }
}
