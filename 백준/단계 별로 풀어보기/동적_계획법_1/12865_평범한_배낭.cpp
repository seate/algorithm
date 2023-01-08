#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <tuple>
using namespace std;

bool second_first(pair<int, int> &a, pair<int, int> &b){
    if (a.second != b.second) return a.second < b.second;
    else return a.first < b.first;
}

int main()
{
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	int N, MAX;
	cin >> N >> MAX;
	
	vector<vector<int>> dp(N + 1, vector<int>(MAX + 1));
	vector<pair<int, int>> data(N);
	for (int i = 0; i < N; i++) cin >> data[i].first >> data[i].second;
	sort(data.begin(), data.end(), second_first);
	sort(data.begin(), data.end());
	
	for (int i = 1; i <= N; i++){
	    for (int j = 1; j <= MAX; j++){
	        if (data[i - 1].first <= j){
	            if (data[i - 1].second + dp[i - 1][j - data[i - 1].first] < dp[i - 1][j]) dp[i][j] = dp[i - 1][j];
	            else dp[i][j] = data[i - 1].second + dp[i - 1][j - data[i - 1].first];
	        }
	        else dp[i][j] = dp[i - 1][j];
	    }
	}
	
	cout << dp[N][MAX];
}