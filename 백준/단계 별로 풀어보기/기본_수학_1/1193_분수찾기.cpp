#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	int N, s = 1, y;
	cin >> N;
	N *= 2;
	
	while (true)
	{
	    if (N <= s * (s + 1)) break;
	    s += 1;
	}
	
	y = (N - s * (s - 1)) / 2;
	
	if (s & 1) cout << s - y + 1 << "/" << y;
	else cout << y << "/" << s - y + 1;
}