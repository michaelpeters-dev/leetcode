#include <bits/stdc++.h>
using namespace std;

int main(){
    int c;
    cin >> c;
    while(c--){
        int n, k;
        cin >> n;
        bool flag = true;
        for (int i = 0; i<n; i++){
            cin >> k;
            if (i>0 && k==1){
                flag = false;
            }
        }
        cout <<(flag ? "YES" : "NO")<< "\n";
    }
}
