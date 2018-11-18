#include <algorithm> // sorting
#include <iostream>  // I/O
#include <vector>    // container
using namespace std;
int main() {
    int input;
    vector<int> ivec;
    // input
    while (cin >> input)
        ivec.push_back(input);
    // sorting
    sort(ivec.begin(), ivec.end());
    // output
    vector<int>::iterator it;
    for (it = ivec.begin(); it != ivec.end(); ++it) {
        cout << *it << " ";
    }
    cout << endl;
    return 0;
}