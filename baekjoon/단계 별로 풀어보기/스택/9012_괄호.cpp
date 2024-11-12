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
	
	int T;
	cin >> T;
	string S;
	
	while (T--){
	    int count = 0;
	    cin >> S;
	    for (auto &s : S){
	        if (s == '(') count++;
	        else count--;
	        if (count < 0) break;
	    }
	    cout << ((count == 0) ? "YES" : "NO") << "\n";
	}
}