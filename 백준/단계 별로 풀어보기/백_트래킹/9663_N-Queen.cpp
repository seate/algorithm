#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <tuple>
using namespace std;

int cnt = 0;
int N;
vector<vector<int>> board;

void recursion(int y){
	for (int x = 0; x < N; x++){
		if (board[y][x] == 0){
			if (y == N - 1){
				cnt++;
				return;
			}
			
			int py = y, px = x;
			
			
			//세로
			for (int i = y + 1; i < N; i++) board[i][x]++;
			
			//우하
			py = y; px = x;
			while (py < N && px < N){
				board[py][px]++;
				py++; px++;
			}
			
			//좌하
			py = y; px = x;
			while (py < N && 0 <= px){
				board[py][px]++;
				py++; px--;
			}
			
			
			//실행
			recursion(y + 1);
			
			
			//세로
			for (int i = y + 1; i < N; i++) board[i][x]--;
			
			//우하
			py = y; px = x;
			while (py < N && px < N){
				board[py][px]--;
				py++; px++;
			}
			
			//좌하
			py = y; px = x;
			while (py < N && 0 <= px){
				board[py][px]--;
				py++; px--;
			}
		}
	}
}

void fastest_solve(){
	int answer[16]{0,1,0,0,2,10,4,40,92,352,724,2680,14200,73712,365596};
	cout << answer[N];
}


int main()
{
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	cin >> N;
	
	vector<int> temp(N, 0);
	for (int i = 0; i < N; i++) board.push_back(temp);
	
	recursion(0);
	cout << cnt;
	
	//fastest_solve();
}