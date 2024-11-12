#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	double a;
	int b, c;
	cin >> a >> b >> c;
	
	if (c <= b) cout << "-1";
	else cout << ((int)((a / (c - b) + 1)));
}