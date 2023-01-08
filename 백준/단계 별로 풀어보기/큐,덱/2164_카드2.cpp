#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <tuple>
using namespace std;

int cal(int N){
    int i = 1, n = N / 2;
    while (i < n) i <<= 1;
    if (i != n || !(N & 1)) i >>= 1;
    return i;
}

int main()
{
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	int N;
	cin >> N;
	
	if (N <= 2) cout << N;
	else cout << 4 * (N / 2 - cal(N)) + 2 * (N & 1);
}