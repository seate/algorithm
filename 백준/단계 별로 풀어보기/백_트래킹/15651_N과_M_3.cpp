#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <tuple>
using namespace std;

int result[8] = {0, };

void recursion(int level, int &N, int &M){
    if (level == 0){
        for (int i = 0; i < M; i++) cout << result[i] << " ";
        cout << "\n";
        return;
    }
    
    for (int i = 1; i <= N; i++){
        result[M - level] = i;
        recursion(level - 1, N, M);
    }
}

int main()
{
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	int N, M;
	cin >> N >> M;
	
	recursion(M, N, M);
}