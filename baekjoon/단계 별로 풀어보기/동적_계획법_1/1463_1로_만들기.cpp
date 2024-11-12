#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <tuple>
#include <deque>
using namespace std;

int main()
{
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	int N;
	cin >> N;
	if (N == 1){
	    cout << "0";
	    exit(0);
	}
	vector<int> dp(N + 1);
	
    deque<int> que(1, N);
    
    while (!dp[1]){
        int present = que.front();
        que.pop_front();
        
        if (!(present % 3) && !(dp[present / 3])){
            dp[present / 3] = dp[present] + 1;
            que.push_back(present / 3);
        }
        
        if (!(present % 2) && !(dp[present / 2])){
            dp[present / 2] = dp[present] + 1;
            que.push_back(present / 2);
        }
        
        if (!dp[present - 1]){
            dp[present - 1] = dp[present] + 1;
            que.push_back(present - 1);
        }
    }
    
    cout << dp[1];
}