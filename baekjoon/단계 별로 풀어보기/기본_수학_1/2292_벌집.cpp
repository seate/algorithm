#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	double N, result = 0;
	cin >> N;
	N = (N - 1) / 3;
	
	while (true)
	{
	    if (N <= result * (result + 1)) break;
	    result++;
	}
	cout << result + 1;
}