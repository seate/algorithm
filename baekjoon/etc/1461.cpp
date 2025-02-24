#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <unordered_map>
#include <limits.h>
using namespace std;


int main() {
    int N, M, temp, last = 0;
    scanf("%d %d", &N, &M);

    vector<int> pb;
    vector<int> mb;
    for (int i = 0; i < N; i++) {
        scanf("%d", &temp);
        last = max(last, abs(temp));

        if (0 < temp) {
            pb.push_back(temp);
        }
        else {
            mb.push_back(-temp);
        }
    }

    sort(pb.begin(), pb.end(), greater<int>());
    sort(mb.begin(), mb.end(), greater<int>());

    int result = 0;
    for (int i = 0; i < pb.size(); i += M) {
        result += pb[i];
    }
    for (int i = 0; i < mb.size(); i += M) {
        result += mb[i];
    }
    
    printf("%d", result * 2 - last);
}