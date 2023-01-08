#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	int N, count, remain;
	cin >> N;
	count = N / 5;
	remain = N % 5;
	
	while (0 < count and remain % 3 != 0)
	{
	    count--;
	    remain += 5;
	}
	
	if (remain % 3 != 0) cout << "-1";
	else cout << count + remain / 3;
}