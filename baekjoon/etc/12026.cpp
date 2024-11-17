#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <unordered_map>
#include <limits.h>
using namespace std;

#define MAX 10000000

vector<char> c({'B', 'O', 'J'});
unordered_map<char, int> boj = {{'B', 0}, {'O', 1}, {'J', 2}};

char getBefore(char cur) {
    int i = boj[cur] - 1;
    if (i < 0) i = boj.size() - 1;

    return c[i];
}

int main()
{
    int N;
    string s;
    scanf("%d", &N);
    cin >> s;
    
    //*
    vector<int> dp(N, MAX);
    dp[0] = 0;


    for (int i = 1; i < N; i ++) {
        char cur = s[i];
        char before = getBefore(cur);
        for (int j = 0; j < i; j++) {
            if (s[j] == before) {
                dp[i] = min(dp[i], dp[j] + (i - j) * (i - j));
            }
        }
    }
    

    /*
    for (int d : dp) {
        printf("%d ", d);
    }
    printf("\n");
    //*/

    if (dp.back() == MAX) {
        printf("-1");
    }
    else {
        printf("%d", dp.back());
    }

//*/
}