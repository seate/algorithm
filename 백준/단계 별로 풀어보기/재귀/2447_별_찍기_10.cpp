#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;

void recursion_solve()
{
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	int N;
	cin >> N;
	int block_term = N;
	int term_length = N / 3;
	int repeat = 1;
	
	vector<vector<char>> board;
	for (int i = 0;i < N; i++){
		vector<char> temp;
    	for (int j = 0; j < N; j++) temp.push_back('*');
	    board.push_back(temp);
	}
	
	while (repeat != N){
		int start_y = term_length;
		for (int y = 0; y < repeat; y++){
			int start_x = term_length;
			for (int x = 0; x < repeat; x++){
				for (int s_y = start_y; s_y < start_y + term_length; s_y++){
					for (int s_x = start_x; s_x < start_x + term_length; s_x++) board[s_y][s_x] = ' ';
				}
				start_x += block_term;
			}
			start_y += block_term;
		}
		term_length /= 3;
		block_term /= 3;
		repeat *= 3;
	}
	
	for (auto each : board){
		for (auto i : each) cout << i;
		cout << '\n';
	}
}

//=========================================================================================

vector<string> concatenate(vector<string> &r1, vector<string> &r2){
	vector<string> str;
	for (int i = 0; i < r1.size(); i++) str.push_back(r1[i] + r2[i] + r1[i]);
	return str;
}

vector<string> star10(int n, const int N){
	if (n == 1){
		vector<string> temp(1, "*");
		return temp;
	}
	
	n /= 3;
	vector<string> x = star10(n, N);
	vector<string> a = concatenate(x, x);
	
	string line_temp;
	vector<string> temp1;
	for (int i = 0; i < n; i++) line_temp += " ";
	for (int i = 0; i < n; i++) temp1.push_back(line_temp);
	
	vector<string> b = concatenate(x, temp1);
	
	vector<string> connected;
	connected.insert(connected.end(), a.begin(), a.end());
	connected.insert(connected.end(), b.begin(), b.end());
	connected.insert(connected.end(), a.begin(), a.end());
	
	return connected;
}

void fastest_solve(){
	int N;
	cin >> N;
	vector<string> result = star10(N, N);
	for (auto line : result) cout << line << '\n';
}

int main(){
	//recursion_solve();
	fastest_solve();
}