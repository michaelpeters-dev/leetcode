#include <bits/stdc++.h>
using namespace std;

int main(){
    int t;
    cin >> t;

    int minimum = INT_MAX;
    for (int i = 0; i<t; i++){
        int num;
        cin >> num;

        if (abs(num)<abs(minimum)){
            minimum = num;
        }
    }
    
    cout << abs(minimum) << "\n";
}
