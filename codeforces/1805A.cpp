#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        int s = 0;
        for (int i = 0; i<n; i++) {
            int tmp;
            cin >> tmp;
            s ^= tmp;
        }

        if (n%2==0 && s!=0) {
            cout << "-1\n";
        } else if (n%2 == 0 && s==0) {
            cout << 0 << "\n";
        } else {
            cout << s << "\n";
        }
    }
}
