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
	vector<vector<unsigned long long int>> dp(N, vector<unsigned long long int>(10, 1));
	dp[0][0] = 0;
	unsigned long long int MOD = 1000000000;
	
	for (int y = 1; y < N; y++){
	    dp[y][0] = dp[y - 1][1];
	    for (int x = 1; x < 9; x++) dp[y][x] = dp[y - 1][x - 1] + dp[y - 1][x + 1] % MOD;
	    dp[y][9] = dp[y - 1][8];
	}
	
	
	long long int result = 0;
	for (auto i : dp[N - 1]){
	    result += i % 1000000000;
	    result %= 1000000000;
	}
	
	cout << result << "\n";
}