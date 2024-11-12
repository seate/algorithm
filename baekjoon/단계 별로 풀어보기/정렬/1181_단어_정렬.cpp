#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;

bool compare(string &s1, string &s2){
    if (s1.size() == s2.size()) return s1.compare(s2) < 0;
    else return s1.size() < s2.size();
}


int main()
{
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	int N;
	cin >> N;
	
	vector<string> word;
	for (int i = 0; i < N; i++){
	    string temp;
	    cin >> temp;
	    word.push_back(temp);
	}
	sort(word.begin(), word.end(), compare);
	word.erase(unique(word.begin(), word.end()), word.end());
	
	for (auto each : word) cout << each << "\n";
}