#include <bits/stdc++.h>
using namespace std;

int main(){
    int t;
    cin >> t;
    while(t--){
        vector<string> grid(10); //Creating the grid
        for (int i = 0; i<10; i++){
            cin >> grid[i];
        }

        int score = 0;

        for (int i = 0; i<10; i++){
            for (int j = 0; j<10; j++){
                if (grid[i][j]=='X'){
                    score += min({i, 9-i, j, 9-j}) + 1;
                }
            }
        }

        cout << score << "\n";
    }
}
