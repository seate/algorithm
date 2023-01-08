#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <tuple>
using namespace std;

#define MOD 10007

int main()
{
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	int N, K;
	cin >> N >> K;
	
	vector<vector<int>> dp(N + 2, vector<int>(N + 2));
	dp[1][1] = 1;
	
	for (int i = 2; i <= N + 1; i++){
		for (int j = 1; j <= N + 1; j++) dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % MOD;
	}
	
	cout << dp[N + 1][K + 1];
}