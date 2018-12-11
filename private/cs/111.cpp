#include <algorithm> // sorting
#include <iostream>  // I/O
#include <vector>    // container
using namespace std;
int main() {
    int input;
    vector<vector<int>*> ivec;
    // input
    ivec.push_back(new vector<int>(20,3));
    // sorting
    sort((*ivec[0]).begin(), (*ivec[0]).end());
    // output
    vector<int>::iterator it;
    for (it = (*ivec[0]).begin(); it != (*ivec[0]).end(); ++it) {
        cout << *it << " ";
    }
    delete ivec[0];
    cout << endl;
    return 0;
}