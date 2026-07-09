#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;

        vector<int> a(n);
        int total_r = 0;

        for (int i = 0; i< n; i++) {
            cin >> a[i];
            if (a[i] == 2) total_r++;
        }

        int l = 0;
        int r = total_r;

        int store = -1;

        for (int i = 0; i < n- 1; i++) {
            if (a[i] == 2) {
                l++;
                r--;
            }

            if (l==r) {
                store = i + 1;
                break;
            }
        }

        cout << store << "\n";
    }
}
