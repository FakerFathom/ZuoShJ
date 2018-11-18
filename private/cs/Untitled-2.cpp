#include <bits/stdc++.h>
using namespace std;
const int n = 20;
class sb {
public:
	char *p;
	sb() {
		p = new char[n];
		p = "sbsbjiushiwo";
	}
	sb(sb A) : sb() {
		for (int i = 0; i < n; ++i)
			p[i] = A.p[i];
		cout << "A\n";
	}
	sb(sb &A) : sb() {
		for (int i = 0; i < n; ++i)
			p[i] = A.p[i];
		cout << "&A\n";
	}
	sb(sb &&A) : sb() {
		for (int i = 0; i < n; ++i)
			p[i] = A.p[i];

		cout << "&&A\n";
	}
	void show() {
		cout << p << endl;
		cout << "yes\n";
	}

	sb friend operator+(sb a, sb b) {
		sb c;
		for (int i = 0; i < n; ++i)
			c.p[i] = a.p[i] + b.p[i] - 97;
		return c;
	}
};

int main() {
	sb a;
	a.show();
	cout << "hei";
	sb b(a);
	b.show();
	cout << "biu";
	sb c(a + b);
	c.show();
	return 0;
}