#include <bits/stdc++.h>
using namespace std;

int main(){
    int t;
    cin >> t;

    while(t--){
        int n;
        cin >> n;

        vector<int> a;

        for(int i = 0; i < n; i++){
            int temp;
            cin >> temp;
            a.push_back(temp);
        }

        sort(a.begin(), a.end());

        int mn = a[0];

        vector<int> b, c;

        for(int i = 0; i < n; i++){
            if(a[i] == mn)
                b.push_back(a[i]);
            else
                c.push_back(a[i]);
        }

        if(b.empty() || c.empty()){
            cout << "-1\n";
        }
        else{
            cout << b.size() << " " << c.size() << "\n";

            for(int x : b) cout << x << " ";
            cout << "\n";

            for(int x : c) cout << x << " ";
            cout << "\n";
        }
    }
}

