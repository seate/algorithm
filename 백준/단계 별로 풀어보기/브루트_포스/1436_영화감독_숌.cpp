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
	
	int N, present = 666;
	cin >> N;
	
	while (N){
	    if (to_string(present).find("666") != -1) N--;
	    present++;
	}
	cout << present - 1;
}