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
	
	int N, MAX, temp, result = 0;
	vector<int> nums;
	cin >> N >> MAX;
	for (int i = 0; i < N; i++){
	    cin >> temp;
	    nums.push_back(temp);
	}
	
	for (int i = 0; i < N - 2; i++){
	    for (int j = i + 1; j < N - 1; j++){
	        for (int k = j + 1; k < N; k++){
	            int present = nums[i] + nums[j] + nums[k];
	            if (present == MAX){
	                result = MAX;
	                break;
	            }
	            if (result < present && present < MAX) result = present;
	        }
	    }
	}
	cout << result;
}