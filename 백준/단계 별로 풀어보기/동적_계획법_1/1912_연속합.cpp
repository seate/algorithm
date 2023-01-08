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
	
	int N;
	cin >> N;
	vector<int> data(N);
	for (int i = 0; i < N; i++) cin >> data[i];
	
	vector<int> dp(1, data[0]);
	for (int i = 1; i < N; i++) dp.push_back((dp.back() <= 0) ? data[i] : dp.back() + data[i]);
	
	cout << *max_element(dp.begin(), dp.end());
}