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
	for (auto &d : data) cin >> d;
	sort(data.begin(), data.end());
	
	cout << data.front() * data.back();
}