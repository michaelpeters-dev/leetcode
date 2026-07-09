// Look for infinite water sources or else count all the water sources
#include <bits/stdc++.h>
using namespace std;

int main(){
    int t;
    cin >> t;
    while (t--){
        int n;
        string s;
        cin >> n >> s;

        bool hasThree = false;
        for (int i = 2; i < n + 2; i++){
            if (s[i-2]=='.' && s[i-1]=='.' && s[i]=='.'){
                hasThree = true;
            }
        }

        if (hasThree){
            cout << 2 << "\n";
        } else {
            cout << count(s.begin(), s.end(), '.') << "\n";
        }
    }
}
