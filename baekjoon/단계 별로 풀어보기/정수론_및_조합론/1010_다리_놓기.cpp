#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <tuple>
using namespace std;

int recursion(int N, int M){
    return !((N - M) * (M)) ? 1 : recursion(N - 1, M - 1) * N / M;
}

int main()
{
    cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
    
    int T, N, M;
	cin >> T;
	while(T--){
		cin >> N >> M;
		cout << recursion(M, N) << "\n";
	}
}