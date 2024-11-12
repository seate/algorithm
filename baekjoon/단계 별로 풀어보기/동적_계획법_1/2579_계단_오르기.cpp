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
	
	vector<int> weight(N);
	for (int i = 0; i < N; i++) cin >> weight[i];
	
	vector<int> dp(N);
	dp[0] = weight[0];
	if (2 <= N) dp[1] = weight[0] + weight[1];
	if (3 <= N) dp[2] = max(weight[0], weight[1]) + weight[2];
	
	for (int i = 3; i < N; i++) dp[i] = weight[i] + max(dp[i - 3] + weight[i - 1], dp[i - 2]);
	
	cout << dp[N - 1];
}