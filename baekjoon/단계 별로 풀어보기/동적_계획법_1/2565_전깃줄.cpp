#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <tuple>
using namespace std;

int bisect_left(vector<int> &list, int &finding){
	int S = 0, M = 0, E = list.size() - 1;
	        
    while (S < E){
        M = (S + E) / 2;
        if (finding == list[M]) break;
        else if (finding < list[M]) E = M - 1;
        else S = M + 1;
    }
    
    if (list[M] != finding){
    	if (list[S] < finding) return S + 1;
    	else return S;
    }
    return M;
}

int main()
{
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	int N;
	cin >> N;
	
	vector<pair<int, int>> original_data(N);
	for (int i = 0; i < N; i++) cin >> original_data[i].first >> original_data[i].second;
	sort(original_data.begin(), original_data.end());
	
	vector<int> data(N);
	for (int i = 0; i < N; i++) data[i] = original_data[i].second;
	
	vector<int> min_list(1, data[0]);
	
	for (auto &present : data){
	    if (min_list[min_list.size() - 1] < present) min_list.push_back(present);
	    else min_list[bisect_left(min_list, present)] = present;
	}
	
	cout << N - min_list.size();
}