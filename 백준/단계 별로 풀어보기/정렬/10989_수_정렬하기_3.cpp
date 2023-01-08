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
	
	int count[10001] = {0, };
	
	int N, temp;
	cin >> N;
	for (int i = 0; i < N; i++){
	    cin >> temp;
	    count[temp]++;
	}
	
	for (int i = 1; i < 10001; i++){
	    for (int j = 0; j < count[i]; j++) cout << i << "\n";
	}
}