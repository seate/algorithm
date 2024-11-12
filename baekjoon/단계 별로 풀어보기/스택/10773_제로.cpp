#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <tuple>
using namespace std;

int sum(vector<int> &arr){
    int S = 0;
    for (auto &s : arr) S += s;
    return S;
}

int main()
{
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	vector<int> stack;
	int T, input;
	cin >> T;
	
	while (T--){
	    cin >> input;
	    if (input) stack.push_back(input);
	    else stack.pop_back();
	}
	
	cout << sum(stack);
}