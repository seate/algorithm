#include <iostream>
#include <vector>
#include <string>
#include <cmath>
using namespace std;

int main()
{
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	int N, d = 2;
	cin >> N;
	int sqrtN = (int)sqrt(N) + 1;
	while (d <= sqrtN){
	    while (!(N % d)){
	        cout << d << '\n';
	        N /= d;
	    }
	    d++;
	}
	if (1 < N) cout << N;
}