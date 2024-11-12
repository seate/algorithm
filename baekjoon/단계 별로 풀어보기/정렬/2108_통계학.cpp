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
	
	int N, temp, sum = 0, counter[8001] = {0, };
	vector<int> nums;
	cin >> N;
	for (int i = 0; i < N; i++){
	    cin >> temp;
	    nums.push_back(temp);
	    sum += temp;
	    counter[temp + 4000]++;
	}
	sort(nums.begin(), nums.end());
	
	cout << floor(sum / (float)N + 0.5) << "\n";
	cout << nums[N / 2] << "\n";
	
	int Max = 0;
	vector<int> sames;
	for (int i = 0; i < 8001; i++){
	    if (Max == counter[i]) sames.push_back(i);
	    else if (Max < counter[i]){
	        sames.clear();
	        sames.push_back(i);
	        Max = counter[i];
	    }
	}
	
	if (2 <= sames.size()){
	    sort(sames.begin(), sames.end());
	    cout << sames[1] - 4000 << "\n";
	}
	else cout << sames[0] - 4000 << "\n";
	
	cout << nums[N - 1] - nums[0];
}