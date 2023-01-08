#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	string A, B, temp;
	cin >> A >> B;
	
	int present, up = 0;
	int longer = max(A.size(), B.size()), shorter = min(A.size(), B.size());
	string result(longer, '0');
	
	for (int i = 0; i < longer - shorter; i++) temp += "0";
	
	if (A.size() < B.size()) A = temp + A;
	else B = temp + B;
	
	for (int i = longer - 1; 0 <= i; i--)
	{
	    present = (A[i] - '0') + (B[i] - '0') + up;
	    up = present / 10;
	    result[i] = (present % 10) + '0';
	}
	
	if (up != 0) cout << up;
	for (int i = 0; i < longer; i++) cout << result[i];
}