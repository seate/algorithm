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
	
	if (N < 3){
	    if (N == 1) cout << weight[0];
	    else cout << weight[0] + weight[1];
	    exit(0);
	}
	
	vector<int> dp(N);
	dp[0] = weight[0];
	dp[1] = weight[0] + weight[1];
	dp[2] = dp[1] + weight[2] - *min_element(weight.begin(), weight.begin() + 3);
	for (int i = 3; i < N; i++){
	    int temp = ((dp[i - 2] < dp[i - 3] + weight[i - 1]) ? dp[i - 3] + weight[i - 1] : dp[i - 2]) + weight[i];
	    dp[i] = ((dp[i - 1] < temp) ? temp : dp[i - 1]);
	}
	
	cout << dp[N - 1];
}