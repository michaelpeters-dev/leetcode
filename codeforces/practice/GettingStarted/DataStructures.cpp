#include <bits/stdc++.h>
using namespace std;

int main() {
  // array<int, 5> arr; // Array
  vector<int> vec; // Dynamic Array
  
  for (vector<int>::iterator it = vec.begin(); it != vec.end(); ++it) { // Looping through an array
    cout << *it << " ";
  }

  vec.push_back(5); // Adding to back
  vec.erase(vec.begin() - 1); // Removes index O(n)
  cout << vec.size() << endl; // This prints the length of the vector
  
  pair<string, int> pair1 = make_pair("Testing", 2); // Creating a pair (can store two different types)
  cout << pair1.first << " " << pair1.second << endl;

  int a = 1;
  int b = 2;
  int c = 3;
  tuple<int, int, int> t = tie(a, b, c);
  cout << get<0>(t) << endl; // get<T>(t) T must be a contant


}
