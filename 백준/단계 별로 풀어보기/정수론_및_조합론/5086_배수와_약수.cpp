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
	
	int a, b;
	while (true){
	    cin >> a >> b;
	    if (!a && !b) break;
	    
	    if (!(a % b)) cout << "multiple\n";
	    else if (!(b % a)) cout << "factor\n";
	    else cout << "neither\n";
	}
}