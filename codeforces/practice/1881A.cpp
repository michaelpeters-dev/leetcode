#include <bits/stdc++.h>
using namespace std;

int main(){
    int t;
    cin >> t;

    while(t--){
        int n, m;
        cin >> n >> m;

        string x, s;
        cin >> x >> s;

        int ops = 0;
        while(x.size() < s.size()){
            x += x;
            ops++;
        }

        if(x.find(s) != string::npos){
            cout<< ops << "\n";
            continue;
        } else{
            x += x;
            ops++;
        }
        
        if (x.find(s) != string::npos){
            cout << ops << "\n";
        } else {
            cout << "-1\n";
        }
    }
}
