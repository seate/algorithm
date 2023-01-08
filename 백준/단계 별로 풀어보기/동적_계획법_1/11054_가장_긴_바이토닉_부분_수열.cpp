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
	vector<int> data(N);
	for (int i = 0; i < N; i++) cin >> data[i];
	
	vector<int> min_list1(1, data[0]);
	vector<int> min_list2(1, data[N - 1]);
	vector<int> dp1;
	vector<int> dp2;
	int MAX = 0;
	
	for (auto &present : data){
	    if (min_list1[min_list1.size() - 1] < present){
	        min_list1.push_back(present);
	        dp1.push_back(min_list1.size());
	    }
	    else{
	        int index = bisect_left(min_list1, present);
	        min_list1[index] = present;
	        dp1.push_back(index + 1);
	    }
	}
	
	for (int i = N - 1; 0 <= i; i--){
		int &present = data[i];
	    if (min_list2[min_list2.size() - 1] < present){
	        min_list2.push_back(present);
	        dp2.push_back(min_list2.size());
	    }
	    else{
	        int index = bisect_left(min_list2, present);
	        min_list2[index] = present;
	        dp2.push_back(index + 1);
	    }
	}
	
	
	for (int i = 0; i < dp1.size(); i++){
		if (MAX < dp1[i] + dp2[N - i - 1]) MAX = dp1[i] + dp2[N - i - 1];
	}
	
	cout << MAX - 1;
}