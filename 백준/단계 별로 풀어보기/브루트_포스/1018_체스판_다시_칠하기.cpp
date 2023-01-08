#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;

int main()
{
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	int vertical, horizontal, result = 99999999;
	vector<string> board;
	
	cin >> vertical >> horizontal;
	for (int i = 0; i < vertical; i++){
	    string temp;
	    cin >> temp;
	    board.push_back(temp);
	}
	
	for (int start_y = 0; start_y < vertical - 7; start_y++){
	    for (int start_x = 0; start_x < horizontal - 7; start_x++){
	        int w_count = 0, b_count = 0;
	        for (int y = start_y; y < start_y + 8; y++){
	            for (int x = start_x; x < start_x + 8; x++){
	                if ((y & 1 && x & 1) || !(y & 1 || x & 1)){
	                    if (board[y][x] == 'W') b_count++;
	                    else w_count++;
	                }
	                
	                else{
	                    if (board[y][x] == 'W') w_count++;
	                    else b_count++;
	                }   
	            }
	        }
	        result = min(result, min(w_count, b_count));
	    }
	}
	cout << result;
}