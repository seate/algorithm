#include <iostream>
#include <vector>
#include <math.h>
#include <string>
#include <algorithm>
#include <cmath>
#include <unordered_map>
#include <unordered_set>
#include <limits.h>

using namespace std;


int main() {
    int N;
    int div = 10007;
    
    scanf("%d", &N);

    vector<vector<int>> dp(N, vector<int>(10, 1));
    for (int i = 1; i < N; i++) {
        dp[i][0] = dp[i - 1][0];
        for (int j = 1; j < 10; j++) {
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % div;
        }
    }

    int result = 0;
    for (int i = 0; i < 10; i++) {
        result = (result + dp[N - 1][i]) % div;
    }

    printf("%d", result);
}