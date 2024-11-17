#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <unordered_map>
#include <limits.h>
using namespace std;

int dr[] = {-1, 0, 1};

void recur(vector<vector<bool>> &m, int R, int C, int r, int c, bool &finish) {
    if (C - 1 <= c) {
        finish = true;
        return;
    }

    
    for (int i = 0; i < 3; i++) {
        int nextR = r + dr[i];
        int nextC = c + 1;
        

        if (nextR < 0 || R <= nextR || !m[nextR][nextC] || finish) continue;

        recur(m, R, C, nextR, nextC, finish);
    }

    m[r][c] = false;    
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int R, C;
    cin >> R >> C;
    vector<vector<bool>> m(R, vector<bool>(C, false));

    string row;
    for (int r = 0; r < R; r++) {
        cin >> row;
        for (int c = 0; c < C; c++) {
            m[r][c] = (row[c] == '.');
        }
    }

    int result = 0;
    for (int r = 0; r < R; r++) {
        bool finish = false;
        recur(m, R, C, r, 0, finish);
        result += finish;
    }

    cout << result;
}