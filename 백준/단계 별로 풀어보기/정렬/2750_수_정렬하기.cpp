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
	
	int N, temp;
	vector<int> nums;
	cin >> N;
	for (int i = 0; i < N; i++){
	    cin >> temp;
	    nums.push_back(temp);
	}
	sort(nums.begin(), nums.end());
	
	for (int i = 0; i < N; i++) cout << nums[i] << '\n';
}