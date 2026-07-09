#include <bits/stdc++.h>
using namespace std;

int main(){
    int c;
    cin >> c;
    while(c--){
        int n, k;
        cin >> n >> k;

        bool flag = false;

        for (int i = 0; i < n; i++){
            int t;
            cin >> t;
            if (t==k){
                flag = true;
            }
        }
        cout << (flag ? "YES\n" : "NO\n");
    }
}
