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
	
	int N, counter[11] = {0, };
	cin >> N;
	N *= 10;
	while (N /= 10) counter[N % 10]++;
	
	for (int i = 10; 0 <= i; i--){
	    for (int j = 0; j < counter[i]; j++) cout << i;
	}
}