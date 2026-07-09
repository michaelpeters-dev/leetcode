#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        string temp;

        for (int i = 0; i < n; i++) {
            char q;
            cin >> q;
            temp += q;
        }
        
        int l = 0;
        int r = n-1;

        while (l < r) {
            if (temp[l]=='1' && temp[r]=='0' || temp[l]=='0' && temp[r]=='1') {
                l += 1;
                r -= 1;
            } else {
                break;
            }
        }

        cout << n - 2*l << "\n";
    }
}
