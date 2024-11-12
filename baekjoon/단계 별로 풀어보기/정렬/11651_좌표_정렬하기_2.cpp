#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;

bool compare(pair<int, int> &a, pair<int, int> &b){
    if (a.second == b.second) return a.first < b.first;
    else return a.second < b.second;
}

int main()
{
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	int N;
	vector<pair<int, int>> coors;
	cin >> N;
	for (int i = 0; i < N; i++){
	    int temp1, temp2;
	    cin >> temp1 >> temp2;
	    coors.push_back(pair<int, int>(temp1, temp2));
	}
	sort(coors.begin(), coors.end(), compare);
	for (int i = 0; i < N; i++) cout << coors[i].first << " " << coors[i].second << "\n";
}