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
	
	
	int T;
	cin >> T;
	
	vector<pair<int, int>> dp;
	dp.push_back(pair<int, int>(1, 0));
	dp.push_back(pair<int, int>(0, 1));
	vector<int> query(T);
	
	int temp;
	for (int i = 0; i < T; i++) cin >> query[i];
	
	int MAX = *max_element(query.begin(), query.end());
	for (int i = 2; i <= MAX; i++) dp.push_back(pair<int, int> (dp[i - 1].first + dp[i - 2].first, dp[i - 1].second + dp[i - 2].second));
	
	for (auto i : query) cout << dp[i].first << " " << dp[i].second << "\n";
}