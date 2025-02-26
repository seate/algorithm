#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <unordered_map>
#include <limits.h>
using namespace std;

int realResult = 0;


void recur(vector<pair<int, int>> eggs, int curIdx) {
    if (eggs.size() <= curIdx) {
        int result = 0;
        for (auto e : eggs) {
            result += (e.first <= 0);
        }
        realResult = max(realResult, result);

        return;
    }


    if (eggs[curIdx].first <= 0) {
        // 현재 계란이 깨졌다면, 그냥 다음 계란으로 넘어간다.
        recur(eggs, curIdx + 1);
        return;
    }

    bool flag = false;
    for (int i = 0; i < eggs.size(); i++) {
        if (i == curIdx) continue;

        if (0 < eggs[i].first) {
            flag = true;

            eggs[curIdx].first -= eggs[i].second;
            eggs[i].first -= eggs[curIdx].second;

            recur(eggs, curIdx + 1);

            eggs[curIdx].first += eggs[i].second;
            eggs[i].first += eggs[curIdx].second;
        }
    }

    if (!flag) {
        recur(eggs, curIdx + 1);
    }
}



int main() {
    int N, t1, t2;
    scanf("%d", &N);

    vector<pair<int, int>> eggs;
    for (int i = 0; i < N; i++) {
        scanf("%d %d", &t1, &t2);
        eggs.push_back(make_pair(t1, t2));
    }

    
    recur(eggs, 0);

    printf("%d", realResult);
}