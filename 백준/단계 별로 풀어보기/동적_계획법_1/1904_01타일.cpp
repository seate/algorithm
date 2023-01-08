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
	
	int N;
	cin >> N;
	vector<int> dp(max(N + 1, 3));
	dp[1] = 1; dp[2] = 2;
	
	for (int i = 3; i <= N; i++) dp[i] = (dp[i - 1] + dp[i - 2]) % 15746;
	
	cout << dp[N];
}