#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	int N, result = 0;
	char nums[100];
	cin >> N >> nums;
	
	for (int i = 0; i < N; i++) result += nums[i] - '0';
	
	cout << result;
}