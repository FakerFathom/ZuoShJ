#include <bits/stdc++.h>
using namespace std;
/* template <class T>
void print(T data)
{
    cout << data << endl;
}
template <class T>
void print(T data, int n_times)
{
    for (int i = 0; i < n_times; i++)
        cout << data << endl;
}
template<int N> */
void printaaa(ofstream f){
    while(!f.eof()){
    string str;
    getline (f,str);
    cout << str << '\n';
    }
}

int  main()
{
    ofstream m;
    printaaa(m);
    return 0;
}