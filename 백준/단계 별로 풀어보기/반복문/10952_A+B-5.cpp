#include <iostream>
#include <vector>
using namespace std;

int main()
{
	cin.tie(NULL);
    ios_base::sync_with_stdio(false);
	
	int a = 1;
	int b = 1;
	
	while (true)
	{
	    cin >> a >> b;
	    if (a == 0 and b == 0) break;
	    cout << a + b << '\n';
	}
	
}