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
	vector<int> query(T);
	for (int i = 0; i < T; i++) cin >> query[i];
	
	int MAX = *max_element(query.begin(), query.end());
	
	vector<long long int> dp(max(MAX + 1, 6), 1);
	dp[4] = 2; dp[5] = 2;
	
	for (int i = 6; i <= MAX; i++) dp[i] = dp[i - 1] + dp[i - 5];
	
	for (auto q : query) cout << dp[q] << "\n";
}