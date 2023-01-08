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
	
	int N;
	cin >> N;
	vector<int> data(N);
	for (auto &d : data) cin >> d;
	int standard = data[0];
	
	for (int i = 1; i < data.size(); i++){
	    int GCD = gcd(standard, data[i]);
	    cout << standard / GCD << "/" << data[i] / GCD << "\n";
	}
}