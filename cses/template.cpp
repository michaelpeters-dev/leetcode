#include <bits/stdc++.h>
using namespace std;

using ll  = long long;
using ull = unsigned long long;
using ld  = long double;
using pii = pair<int,int>;
using pll = pair<ll,ll>;
template<class T> using vc  = vector<T>;
template<class T> using vvc = vector<vector<T>>;
using vi  = vc<int>;
using vll = vc<ll>;
using vpi = vc<pii>;
using vvi = vvc<int>;

#define all(x)   (x).begin(), (x).end()
#define rall(x)  (x).rbegin(), (x).rend()
#define sz(x)    (int)(x).size()
#define pb       push_back
#define eb       emplace_back
#define mp       make_pair
#define fi       first
#define se       second
#define FOR(i,a,b) for (int i = (a); i < (b); ++i)
#define ROF(i,a,b) for (int i = (b)-1; i >= (a); --i)
#define REP(i,n) FOR(i,0,n)
#define each(x,a) for (auto& x : a)

constexpr int  INF  = 1e9 + 7;
constexpr ll   LINF = 4e18;
constexpr int  MOD  = 1e9 + 7;
constexpr ld   EPS  = 1e-9;
constexpr int  dx[] = {1,-1,0,0,1,1,-1,-1};
constexpr int  dy[] = {0,0,1,-1,1,-1,1,-1};

template<class T, class U> bool ckmin(T& a, U b) { return b < a ? a = b, 1 : 0; }
template<class T, class U> bool ckmax(T& a, U b) { return a < b ? a = b, 1 : 0; }

#ifdef LOCAL
  #include "debug.h"
#else
  #define dbg(...) 42
#endif

void solve() {
    // your code here
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T = 1;
    // cin >> T;
    while (T--) solve();
    return 0;
}
