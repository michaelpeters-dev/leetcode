#include <bits/stdc++.h>
using namespace std;

int main(){
    int t;
    cin >> t;
    while (t--){
        int n;
        cin >> n;

        int pos = 0;
        int neg = 0;
        for (int i = 0; i<n; i++){
            int tmp;
            cin >> tmp;
            if (tmp==1) pos++;
            else neg++;
        }

        int ops = 0;
        while (pos<neg){
            pos++;
            neg--;
            ops++;
        }
        if (neg%2==1){
            ops++;
        }
        cout << ops << "\n";
    }
}
