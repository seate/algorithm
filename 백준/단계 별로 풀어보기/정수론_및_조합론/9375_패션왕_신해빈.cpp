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
	
	while (T--){
		int N, result = 1;
		vector<int> counter;
		vector<string> kind;
		
		cin >> N;
		
		string s, k;
		while (N--){
			cin >> s >> k;
			auto index = find(kind.begin(), kind.end(), k);
			
			if (index == kind.end()){
				kind.push_back(k);
				counter.push_back(1);
			}
			else counter[index - kind.begin()]++;
		}
		
		for (auto &i : counter) result *= (i + 1);
		cout << result - 1 << "\n";
	}
}