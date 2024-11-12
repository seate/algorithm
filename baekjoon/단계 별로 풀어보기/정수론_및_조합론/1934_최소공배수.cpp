#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <tuple>
using namespace std;

int gcd(int a, int b){
    if (a < b){
        int temp = a;
        a = b;
        b = temp;
    }
    int n;
    while (b){
        n = a % b;
        a = b;
        b = n;
    }
    return a;
}

int main()
{
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	int T, a, b;
	cin >> T;
	while (T--){
    	cin >> a >> b;
    	cout << a * b / gcd(a, b) << "\n";
	}
}