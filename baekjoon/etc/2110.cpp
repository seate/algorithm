#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <unordered_map>
#include <limits.h>
using namespace std;


int main() {
    int N, C;

    scanf("%d %d", &N, &C);

    vector<int> houses(N);
    for (int i = 0; i < N; i++) {
        scanf("%d", &houses[i]);
    }
    sort(houses.begin(), houses.end());

    int result = 0;
    int start = 1;
    int end = houses[houses.size() - 1] - houses[0];

    while (start <= end) {
        int mid = (start + end) / 2;

        int count = 1; // 1 -> 첫 집
        int prev = houses[0];

        for (int i = 1; i < houses.size(); i++) {
            if (mid <= houses[i] - prev) {
                prev = houses[i];
                count++;
            }
        }

        if (C <= count) {
            result = max(result, mid);
            start = mid + 1;
        }
        else end = mid - 1;
    }

    printf("%d", result);
}