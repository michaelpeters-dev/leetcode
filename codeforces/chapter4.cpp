#include <bits/stdc++.h>
using namespace std;

int main(){
    vector<int> v;
    // or vector<int> v(10), this is a vector with an inital capacity of 10
    v.push_back(3);
    v.push_back(22);
    v.push_back(3);
    for (auto x: v){
        cout<<x<<"\n";
    }

    set<int> s;
    s.insert(2);
    s.insert(4);
    s.insert(5);
    //cout<<s.count(2)<<"\n";
    cout<<"This is the start of the set\n";
    for (auto x: s){
        cout<<x<<"\n";
    }

    cout<<"This is the start of the map\n";
    map<string, int> m;
    m["monkey"] = 4;
    cout<<m["monkey"]<<"\n";

    cout<<"This is the start of a map\n";
    stack<int> sta;
    sta.push(5);
    sta.push(9);
    sta.pop();

    queue<int> q;
    q.push(3);
    q.pop();

    priority_queue<int> pq;
    pq.push(4);
    pq.pop();
}
