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
	for (int i = 0; i < N; i++) cin >> data[i];
	
	vector<int> min_list(1, data[0]);
	
	for (auto present : data){
	    if (min_list[min_list.size() - 1] < present) min_list.push_back(present);
	    else{
	        int S = 0, M = 0, E = min_list.size() - 1;
	        
	        while (S < E){
	            M = (S + E) / 2;
	            if (present == min_list[M]) break;
	            else if (present < min_list[M]) E = M - 1;
	            else S = M + 1;
	        }
	        
	        if (min_list[M] != present){
	        	if (min_list[S] < present) min_list[S + 1] = present;
	        	else min_list[S] = present;
	        }
	    }
	}
	
	cout << min_list.size();
}