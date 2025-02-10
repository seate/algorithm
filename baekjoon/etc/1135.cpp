#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <unordered_map>
#include <limits.h>
using namespace std;


int main() {
    int N, temp;
    scanf("%d", &N);

    vector<vector<int>> childs(N, vector<int>());
    vector<int> parent;
    vector<int> time(N, 0);

    scanf("%d", &temp);
    for (int i = 1; i < N; i++) {
        scanf("%d", &temp);
        parent.push_back(temp);

        childs[temp].push_back(i);
    }


    for (int p = N - 1; 0 <= p; p--) {
        vector<int> curChilds = childs[p];

        vector<int> curTimes;
        for (int curC : curChilds) {
            curTimes.push_back(time[curC]);
        }
        sort(curTimes.begin(), curTimes.end());


        for (int i = 1; i <= curTimes.size(); i++) {
            curTimes[i - 1] += (curTimes.size() - (i-1));
        }

        int curMax = 0;
        for (int i = 1; i <= curTimes.size(); i++) {
            curMax = max(curMax, curTimes[i - 1]);
        }

        time[p] = curMax;
    }

    printf("%d", time[0]);
}