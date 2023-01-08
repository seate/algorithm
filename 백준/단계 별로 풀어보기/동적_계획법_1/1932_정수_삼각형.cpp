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
	
	vector<vector<int>> dp;
	for (int y = 0; y < N; y++){
	    vector<int> temp(y + 1);
	    for (int x = 0; x <= y; x++) cin >> temp[x];
	    dp.push_back(temp);
	}
	
	for (int y = 1; y < N; y++){
	    dp[y][0] += dp[y - 1][0];
	    for (int x = 1; x < y; x++) dp[y][x] += max(dp[y - 1][x - 1], dp[y - 1][x]);
	    dp[y][y] += dp[y - 1][y - 1];
	}
	
	cout << *max_element(dp[N - 1].begin(), dp[N - 1].end());
}