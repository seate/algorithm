#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <tuple>
using namespace std;

int counter(int n, int d){
    int count = 0;
    while (n){
        n /= d;
        count += n;
    }
    return count;
}

int main()
{
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	int N, M;
	cin >> N >> M;
	
	cout << min(counter(N, 5) - counter(M, 5) - counter(N - M, 5), counter(N, 2) - counter(M, 2) - counter(N - M, 2));
}