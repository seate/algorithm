#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <tuple>
using namespace std;

int main()
{
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	int N, count = 0, rest;
	cin >> N >> rest;
	
	vector<int> unit(N);
	for (int i = 0; i < N; i++) cin >> unit[i];
	
	for (int i = N - 1; 0 <= i; i--){
	    if (rest < unit[i]) continue;
	    count += rest / unit[i];
	    rest %= unit[i];
	}
	
	cout << count;
}