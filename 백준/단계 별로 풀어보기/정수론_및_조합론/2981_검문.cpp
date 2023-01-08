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
	sort(data.begin(), data.end());
	
	vector<int> differs(N - 1);
	for (int i = 1; i < N; i++) differs.push_back(data[i] - data[i - 1]);
	
	int GCD = differs[0];
	for (auto &d : differs) GCD = gcd(d, GCD);
	
	vector<int> result1;
	vector<int> result2;
	for (int i = 1; i < (int)sqrt(GCD) + 1; i++){
	    if (GCD % i == 0){
	        result1.push_back(i);
	        result2.push_back(GCD / i);
	    }
	}
	
	for (int i = 1; i < result1.size(); i++) cout << result1[i] << " ";
	for (int i = result2.size() - 1 - (result1.back() == result2.back()); 0 <= i; i--) cout << result2[i] << " ";
}