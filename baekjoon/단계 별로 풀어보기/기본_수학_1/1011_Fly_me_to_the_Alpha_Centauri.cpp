#include <iostream>
#include <vector>
#include <string>
#include <cmath>
using namespace std;

int main()
{
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	int T, x, y, sq;
	cin >> T;
	
	while (T--)
	{
	    cin >> x >> y;
	    sq = (int)sqrt(y - x - 1);
	    if (sq * sq + sq < y - x) cout << 2 * sq + 1 << '\n';
	    else cout << 2 * sq << '\n';
	}
}