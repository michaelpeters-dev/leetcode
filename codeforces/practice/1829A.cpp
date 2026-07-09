#include <bits/stdc++.h>
using namespace std;

int main(){
    int t;
    cin >> t;
    while (t--){
        int n;
        cin >> n;

        int longest = 0;
        int prev = -1;
        int curr = 0;

        for (int i = 0; i<n; i++) {
            int tmp;
            cin >> tmp;
            if (tmp==0) {
                curr += 1;
                longest = max(longest, curr);
            } else {
                curr = 0;
            }
            prev = tmp;
        }
        cout << longest << "\n";
    }
}
