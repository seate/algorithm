#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <unordered_map>
#include <limits.h>
using namespace std;

int main()
{
    int N, lastB = 0, lastO = -1, lastJ = -1;
    string s;

    scanf("%d", &N);
    scanf("%s", s);

    vector<int> dp(N, INT_MAX);

    unordered_map<char, int> boj;

    boj['B'] = 0;
    boj['O'] = 1;
    boj['J'] = 2;




    char curChar;
    for (int i = 1; i < N; i ++) {
        curChar = s[i];

        

        
        
        

    }

}