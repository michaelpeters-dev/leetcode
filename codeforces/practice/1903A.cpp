#include <bits/stdc++.h>
using namespace std;

int main(){
    int c;
    cin >> c;

    while(c--){
        int n, k;
        cin >> n >> k;
        
        vector<int> a(n);
        for (int i = 0; i < n; i++){
            cin >> a[i];
        }

        if (k==1){
            bool ok = true;
            for(int i = 1; i<n; i++){
                if(a[i] < a[i-1]){
                    ok = false;
                }
            }
            cout << (ok ? "YES\n" : "NO\n");
        }
        else{
            cout<<"YES\n";
        }
    }
}
