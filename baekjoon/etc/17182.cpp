/*
백트래킹을 통해 중복 방문을 최소값으로 자동으로 거르면 전부 방문하게 되는데, 그 과정에서 a -> b로 넘어갈 때 최소 거리를 모르니까 플로이드 워셜이 필요하다
*/

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <unordered_map>
#include <limits.h>
#include <queue>
using namespace std;

int N, S, temp;
vector<vector<int>> cost(20, vector<int>(20, 0));
vector<bool> visited(20, false);
vector<int> trace;
int result = 2000000000;

void backtracking(int visitedCount) {
    if (visitedCount == N - 1) {
        int curResult = 0;
        for (int i = 0; i < trace.size() - 1; i++) {
            curResult += cost[trace[i]][trace[i + 1]];
        }
        result = min(result, curResult);
        
        return;
    }

    for (int i = 0; i < N; i++) {
        if (!visited[i]) {
            visited[i] = true;
            trace.push_back(i);
            backtracking(visitedCount + 1);
            trace.pop_back();
            visited[i] = false;
        }
    }
}

int main() {
    
    cin >> N >> S;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> temp;
            cost[i][j] = temp;
        }
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (i == j) continue;

            for (int k = 0; k < N; k++) {
                if (i == k || j == k) continue;

                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j]);
            }
        }
    }

    visited[S] = true;
    trace.push_back(S);

    backtracking(0);

    cout << result;
}