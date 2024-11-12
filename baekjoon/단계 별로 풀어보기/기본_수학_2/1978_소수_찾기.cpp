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
	
	int N, input, count = 0;
	bool isit;
	cin >> N;
	
	for (int i = 0; i < N; i++)
	{
	    isit = true;
	    cin >> input;
	    if (input == 1) isit = false;
	    for (int j = 2; j <= sqrt(input); j++)
	    {
	        if (input % j == 0){
	            isit = false;
	            break;
	        }
	    }
	    if (isit) count += 1;
	}
	cout << count;
}