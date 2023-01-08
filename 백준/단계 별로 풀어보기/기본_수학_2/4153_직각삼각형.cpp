#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;

int main()
{
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	int input, T;
	while (true){
	    vector<int> L;
    	T = 3;
    	while (T--){
    	    cin >> input;
    	    L.push_back(input);
    	}
    	if (L[0] == 0 && L[1] == 0 && L[2] == 0) break;
    	sort(L.begin(), L.end());
    	cout << ((L[0] * L[0] + L[1] * L[1] == L[2] * L[2]) ? ("right\n") : ("wrong\n"));
	}
}