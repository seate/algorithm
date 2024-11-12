#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <tuple>
using namespace std;

vector<vector<vector<int>>> dp(21, vector<vector<int>>(21, vector<int>(21)));

int recursion(int a, int b, int c){
    if (a <= 0 || b <= 0 || c <= 0) return dp[0][0][0];
    else if (20 < a || 20 < b || 20 < c) return dp[20][20][20];
    
    if (!dp[a][b][c]){
        if (a < b && b < c) dp[a][b][c] = recursion(a, b - 1, c) + recursion(a, b, c - 1) - recursion(a, b - 1, c - 1);
        else dp[a][b][c] = recursion(a - 1, b, c) + recursion(a - 1, b - 1, c) + recursion(a - 1, b, c - 1) - recursion(a - 1, b - 1, c - 1);
    }
    return dp[a][b][c];
}


int main()
{
    dp[0][0][0] = 1;
    dp[20][20][20] = 1048576;
	int a, b, c;
	while (true){
	    scanf("%d %d %d", &a, &b, &c);
	    if (a == -1 && b == -1 && c == -1) break;
	    printf("w(%d, %d, %d) = %d\n", a, b, c, recursion(a, b, c));
	}
}