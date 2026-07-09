#include <bits/stdc++.h>
using namespace std;

int main(){
    int c;
    cin>>c;

    for (int _=0; _<c; _++){
        int n, x;
        cin >> n >> x;

        vector<int> d = {0};
        for (int i=0; i<n; i++){
            int tmp;
            cin >> tmp;
            d.push_back(tmp);
        }
        d.push_back(x);
        
        int max = 0;
        for(int t = 1; t<d.size(); t++){
            int diff;
            if (t==d.size()-1){
                diff = 2*(d[t]-d[t-1]);
            }
            else{
                diff = d[t]-d[t-1];
            }
            if (diff>max){
                max = diff;
            }
        }
        cout<<max<<"\n";
    }
}
