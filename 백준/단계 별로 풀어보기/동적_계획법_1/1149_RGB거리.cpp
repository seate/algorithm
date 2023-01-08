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
	vector<vector<int>> dp(N, vector<int>(3));
	
	for (int i = 0; i < N; i++) cin >> dp[i][0] >> dp[i][1] >> dp[i][2];
	
	for (int i = 1; i < N; i++){
	    dp[i][0] += min(dp[i - 1][1], dp[i - 1][2]);
	    dp[i][1] += min(dp[i - 1][0], dp[i - 1][2]);
	    dp[i][2] += min(dp[i - 1][0], dp[i - 1][1]);
	}
	
	cout << *min_element(dp[N - 1].begin(), dp[N - 1].end());
}