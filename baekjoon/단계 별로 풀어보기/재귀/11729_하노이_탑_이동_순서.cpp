#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;

void recursion(int n, int a, int b, int c){
    if (n == 1) cout << a << " " << c << "\n";
    else{
        recursion(n - 1, a, c, b);
        cout << a << " " << c << "\n";
        recursion(n - 1, b, a, c);
    }
}

int main()
{
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	int N;
	cin >> N;
	cout << (int)(pow(2, N) - 1) << "\n";
	recursion(N, 1, 2, 3);
}