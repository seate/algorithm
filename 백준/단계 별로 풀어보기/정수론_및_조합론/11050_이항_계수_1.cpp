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
	
	int N, K;
	cin >> N >> K;
	
	vector<int> dp(N + 1); dp[0] = 1;
	
	for (int i = 1; i <= N; i++) dp[i] = dp[i - 1] * i;
	
	cout << dp[N] / (dp[K] * dp[N - K]);
}