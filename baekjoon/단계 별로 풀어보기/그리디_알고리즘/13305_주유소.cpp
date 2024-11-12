#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <tuple>
using namespace std;

int main()
{
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	long long int N, result = 0;
	cin >> N;
	vector<long long int> distance(N - 1);
	for (auto &d : distance) cin >> d;
	vector<long long int> price(N);
	for (auto &p : price) cin >> p;
	long long int present_min_price = price[0];
	
	for (int i = 0; i < N - 1; i++){
	    if (price[i] < present_min_price) present_min_price = price[i];
	    result += present_min_price * distance[i];
	}
	
	cout << result;
}