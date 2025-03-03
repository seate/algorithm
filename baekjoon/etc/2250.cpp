#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <unordered_map>
#include <unordered_set>
#include <limits.h>
using namespace std;

int curX = 0;

void recur(vector<pair<int, int>> &childs, vector<pair<int,int>> &width, int depth, int cur) {
    // left
    if (childs[cur].first != -1) {
        recur(childs, width, depth + 1, childs[cur].first);
    }

    // current
    width[depth].first = min(curX, width[depth].first);
    width[depth].second = max(curX, width[depth].second);
    curX++;

    // right
    if (childs[cur].second != -1) {
        recur(childs, width, depth + 1, childs[cur].second);
    }
}


int main() {
    int N, t1, t2 ,t3;
    scanf("%d", &N);
    
    vector<pair<int, int>> childs(N + 1, make_pair(-1, -1));
    vector<pair<int,int>> width(N + 1, make_pair(99999999, -1));

    unordered_set<int> noMother;
    for (int i = 1; i <= N; i++) {
        noMother.insert(i);
    }

    for (int i = 0; i < N; i++) {
        scanf("%d %d %d", &t1, &t2, &t3);

        noMother.erase(t2);
        noMother.erase(t3);

        childs[t1].first = t2;
        childs[t1].second = t3;
    }


    for (auto root : noMother) {
        recur(childs, width, 1, root);
        break;
    }

    int maxWidth = 0;
    int maxWidthDepth = 0;
    for (int i = 1; i <= N; i++) {
        if (maxWidth < width[i].second - width[i].first + 1) {
            maxWidth = width[i].second - width[i].first + 1;
            maxWidthDepth = i;
        }
    }

    printf("%d %d", maxWidthDepth, maxWidth);
}