#include <bits/stdc++.h>
#include <numeric>
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
            
        vector<int> a;

        for (int i = 0; i < n; i++) {
            int temp;
            cin >> temp;

            a.push_back(temp);
        }
        
        bool flag = false;
        for (int i = 0; i<n-1; i++) {
            for (int j = i + 1; j<n; j++) {
                if (gcd(a[i], a[j])<=2) {
                    flag = true;
                }
            }
        }

        cout << (flag ? "yes\n" : "no\n");
    }
}
