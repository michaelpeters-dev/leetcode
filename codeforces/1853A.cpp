#include <bits/stdc++.h>
using namespace std;

int main(){
    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        int min_diff = INT_MAX;

        int curr;
        int prev;
        cin >> prev;

        for (int i = 1; i<n; i++){
            cin >> curr;
            if (prev>curr){
                min_diff = 0;
            } else if (prev==curr){
                min_diff = min(min_diff, 1);
            } else {
                min_diff = min(min_diff, curr-prev);
            }
            prev = curr;
        }
        if (min_diff==0){
            cout << "0\n";
        }
        else{
            cout << min_diff/2 + 1 << "\n";
        }
    }
}
