#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;

int factorial(int n){
    if (n <= 2) return n;
    return n * factorial(n - 1);
}

int main()
{
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	int N;
	cin >> N;
	
	if (N) cout << factorial(N);
	else cout << '1';
}