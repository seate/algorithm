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
	
	vector<int> stack;
	for (int i = N - 1; 0 <= i; i--){
	    int D = data[i];
	    while (!stack.empty() && stack.back() <= D) stack.pop_back();
	    data[i] = (!stack.empty()) ? stack.back() : -1;
	    stack.push_back(D);
	}
	for (auto &d : data) cout << d << " ";
}