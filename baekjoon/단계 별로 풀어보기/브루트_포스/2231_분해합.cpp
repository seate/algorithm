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
	
	int N, result = 0;
	cin >> N;
	
	for (int i = max(1, N - 54); i < N; i++){
	   int present = i, temp = i;
	   
	   while (temp){
	       present += temp % 10;
	       temp /= 10;
	   }
	   
	   if (present == N){
	       result = i;
	       break;
	   }
	}
	
	cout << result;
}