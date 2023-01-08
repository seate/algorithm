#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <tuple>
using namespace std;

void get_combinations(int &all_range, int &to_get_element_count, vector<vector<bool>> &result, vector<bool> &one_comb, int start = 0, int depth = 0){
    for (int i = start; i < all_range; i++){
        one_comb[i] = true;
        
        if (depth == to_get_element_count - 1) result.push_back(one_comb);
        else get_combinations(all_range, to_get_element_count, result, one_comb, i + 1, depth + 1);
        
        one_comb[i] = false;
    }
}

void naive_solve()
{
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	int N, half_N, MIN = 65535;
	
	vector<vector<bool>> result;
	
	cin >> N;
	half_N = N / 2;
	
	vector<bool> one_comb(N);
	vector<vector<int>> W(N, vector<int>(N));
	for (int y = 0; y < N; y++){
	    for (int x = 0; x < N; x++) cin >> W[y][x];
	}
	
	get_combinations(N, half_N, result, one_comb);
	
	for (int p = 0; p < result.size() / 2; p++){
		int present_differ = 0;
		
		vector<int> team1;
		vector<int> team2;
		for (int i = 0; i < result[p].size(); i++){
			if (result[p][i]) team1.push_back(i);
			else team2.push_back(i);
		}
		
		for (int i = 0; i < half_N - 1; i++){
			for (int j = i + 1; j < half_N; j++){
				present_differ += (W[team1[i]][team1[j]] + W[team1[j]][team1[i]]) - (W[team2[i]][team2[j]] + W[team2[j]][team2[i]]);
			}
		}
		
		if (abs(present_differ) < MIN) MIN = abs(present_differ);
	}
	
	cout << MIN;
}


//=======================================================================================================================================

void get_combinations2(int &size, int &to_get_element_count, vector<vector<bool>> &result, vector<bool> &one_comb, int start = 0, int depth = 0){
	for (int i = start; i < size; i++){
        one_comb[i] = true;
        
        if (depth == to_get_element_count - 1) result.push_back(one_comb);
        else get_combinations2(size, to_get_element_count, result, one_comb, i + 1, depth + 1);
        
        one_comb[i] = false;
    }
}

void fastest_solve(){
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	int N, MIN = 65535, half_all_sum = 0;
	cin >> N;
	int half_N = N / 2;
	vector<vector<int>> W(N, vector<int>(N));
	vector<int> new_W;
	vector<vector<bool>> result;
	vector<bool> one_comb(N);
	
	for (int y = 0; y < N; y++){
		for (int x = 0; x < N; x++) cin >> W[y][x];
	}
	
	for (int y = 0; y < N; y++){
		int sum = 0;
		for (int x = 0; x < N; x++) sum += W[y][x] + W[x][y];
		new_W.push_back(sum);
		half_all_sum += sum;
	}
	half_all_sum /= 2;
	
	int size = new_W.size() - 1;
	get_combinations2(size, half_N, result, one_comb);
	
	for (auto &line : result){
		int present = 0;
		for (int j = 0; j < line.size(); j++){
			if (line[j]) present += new_W[j];
		}
		
		if (abs(half_all_sum - present) < MIN) MIN = abs(half_all_sum - present);
	}
	
	cout << MIN;
}

int main()
{
	//naive_solve();
	fastest_solve();
}