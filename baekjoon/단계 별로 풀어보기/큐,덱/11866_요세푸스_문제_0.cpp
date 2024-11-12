#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <tuple>
#include <deque>
using namespace std;

int main()
{
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	int N, K;
	cin >> N >> K;
	K--;
	
	deque<int> deq(N);
	for (int i = 1; i <= N; i++) deq[i - 1] = i;
	
	vector<int> result;
	
	while (!deq.empty()){
	    for (int i = 0 ; i < K; i++){
	        deq.push_back(deq.front());
	        deq.pop_front();
	    }
	    result.push_back(deq.front());
	    deq.pop_front();
	}
	
	cout << "<";
	for (int i = 0; i < N - 1; i++) cout << result[i] << ", ";
	cout << result[N - 1] << ">";
}