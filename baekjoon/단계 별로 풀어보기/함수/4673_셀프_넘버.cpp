#include <iostream>
#include <vector>
using namespace std;

int selfNum(int n)
{
    int num_save = n;
    
    while (0 < n)
    {
        num_save += (n % 10);
        n /= 10;
    }
    return num_save;
}

int main()
{
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	vector<bool> v(10036);
	v.assign(10036, false);
	
	for (int i = 0; i < 10000; i++) v[selfNum(i)] = true;
	
	for (int i = 0; i < 10000; i++)
	{
	    if (v[i] == false) cout << i << '\n';
	}
}