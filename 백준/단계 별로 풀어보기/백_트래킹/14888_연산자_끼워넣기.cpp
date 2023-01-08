#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <tuple>
using namespace std;

int N, MAX = -100000001, MIN = 100000001;
vector<int> nums;
vector<int> oper(4, 0);

void recursion(int calculated, int depth = 1){
    if (depth == N){
        if (MAX < calculated) MAX = calculated;
        if (calculated < MIN) MIN = calculated;
        return;
    }
    
    if (oper[0]){
        oper[0]--;
        recursion(calculated + nums[depth], depth + 1);
        oper[0]++;
    }
    
    if (oper[1]){
        oper[1]--;
        recursion(calculated - nums[depth], depth + 1);
        oper[1]++;
    }
    
    if (oper[2]){
        oper[2]--;
        recursion(calculated * nums[depth], depth + 1);
        oper[2]++;
    }
    
    if (oper[3]){
        oper[3]--;
        recursion(calculated / nums[depth], depth + 1);
        oper[3]++;
    }
}


int main()
{
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	int temp;
	cin >> N;
	for (int i = 0; i < N; i++){
	    cin >> temp;
	    nums.push_back(temp);
	}
	
	for (int i = 0; i < 4; i++) cin >> oper[i];
	
	recursion(nums[0]);
	
	cout << MAX << "\n" << MIN;
}