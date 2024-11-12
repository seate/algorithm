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
	int T;
	double x1, y1, r1, x2, y2, r2, center_distance;
	cin >> T;
	while (T--){
	    cin >> x1 >> y1 >> r1 >> x2 >> y2 >> r2;
	    center_distance = sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1));
	    
	    if (x1 == x2 && y1 == y2 && r1 == r2) cout << "-1";
	    else if (r1 + r2 < center_distance) cout << "0";
	    else if (r1 + r2 == center_distance) cout << "1";
	    else if (abs(r1 - r2) < center_distance && center_distance < r1 + r2) cout << "2";
	    else if (abs(r1 - r2) == center_distance) cout << "1";
	    else if (center_distance < abs(r1 - r2)) cout << "0";
	    cout << "\n";
	}
}