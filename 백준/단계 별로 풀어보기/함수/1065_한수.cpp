#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool hansu(int n)
{
    int each_number[3];
    
    for (int i = 0; i < 3; i++)
    {
        each_number[i] = (n % 10);
        n /= 10;
    }
    return bool(each_number[2] - each_number[1] == each_number[1] - each_number[0]);
}

int main()
{
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	int N, count;
	cin >> N;
	
	if (N < 100) cout << N;
	else if (N == 1000) cout << 144;
	else
	{
	    count = 99;
	    for (int i = 100; i < N + 1; i++)
	    {
	        if (hansu(i)) count++;
	    }
	    cout << count;
	}
}