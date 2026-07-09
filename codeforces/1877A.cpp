#include <bits/stdc++.h>
using namespace std;

int main(){
    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;

        int s = 0;
        for (int i=0; i<n-1; i++){
            int temp;
            cin >> temp;
            s += temp;
        }
        s *= -1;
        cout << s << "\n";
    }
}
