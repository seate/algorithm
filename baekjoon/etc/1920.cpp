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
    int N, M, temp;
    unordered_set<int> ns;

    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        scanf("%d", &temp);
        ns.insert(temp);
    }

    scanf("%d", &M);
    for (int i = 0; i < M; i++) {
        scanf("%d", &temp);
        printf("%d\n", (ns.count(temp) != 0));
    }
}