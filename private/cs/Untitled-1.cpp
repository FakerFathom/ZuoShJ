#include <bits/stdc++.h>
using namespace std;
int main() {
	int line=0,column=0;
	int s1[105][105];
	int a[105];
	ifstream inStm;
	inStm.open("afile.txt");
	while( inStm.good() ) {
		string oneLine;
		getline( inStm, oneLine );
		stringstream lineStm(oneLine);
		column-=column;
		while( lineStm.good() ) {
			lineStm >> s1[line][column];
			cout << s1[line][column] << " ";
			++column;
		}
		cout<<endl;
		++line;
	}
	cout << "The number of columns is "<<column<<endl;
	cout<<"Please redefine the order of the columns:";
	for(int i=0; i<column; ++i)cin>>a[i];
	for (int i=0; i<line; ++i) {
		for(int j=0; j<column; ++j)cout << s1[i][a[j]-1] << ' ';
		cout<<"\n";

	}


}
