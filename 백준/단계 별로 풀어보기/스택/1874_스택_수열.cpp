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
	
	bool isit = true;
	int N, index = 0;
	cin >> N;
	vector<int> dest(N);
	for (auto &d : dest) cin >> d;
	
	vector<int> to_stack;
	vector<int> from_stack(N);
	for (int i = 1; i <= N; i++) from_stack[i - 1] = N - i + 1;
	
	vector<char> result;
	
	while (index < N){
	    if (to_stack.empty() || (to_stack[to_stack.size() - 1] < dest[index])){
	        result.push_back('+');
	        to_stack.push_back(from_stack.back());
	        from_stack.pop_back();
	    }
	    
	    else if (to_stack[to_stack.size() - 1] == dest[index]){
	        to_stack.pop_back();
	        result.push_back('-');
	        index++;
	    }
	    
	    else if (dest[index] < to_stack[to_stack.size() - 1]){
	        isit = false;
	        break;
	    }
	}
	
	if (isit){
	    for (auto &r : result) cout << r << "\n";
	}
	else cout << "NO";
}