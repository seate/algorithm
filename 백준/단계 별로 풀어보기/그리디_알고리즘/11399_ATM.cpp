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
	
	int N, result = 0;
	cin >> N;
	
	vector<int> data(N);
	for (auto &d : data) cin >> d;
	sort(data.begin(), data.end());
	
	for (int i = 0; i < N; i++) result += (N - i) * data[i];
	
	cout << result;
}