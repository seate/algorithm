#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <tuple>
using namespace std;

bool second_first(pair<int, int> &a, pair<int, int> &b){
    if (a.second != b.second) return a.second < b.second;
    else return a.first < b.first;
}

int main()
{
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	int N, count = 0, present_end = 0;
	cin >> N;
	vector<pair<int, int>> data(N);
	for (auto &d : data) cin >> d.first >> d.second;
	sort(data.begin(), data.end(), second_first);
	
	for (auto &p : data){
	    if (present_end <= p.first){
	        count++;
	        present_end = p.second;
	    }
	}
	
	cout << count;
}