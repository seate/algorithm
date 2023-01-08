#include <iostream>
using namespace std;

int main()
{
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	int T, a, b;
	int people_box[15][15]{0,};
	
	for (int i = 1; i < 15; i++) people_box[1][i] = i * (i + 1) / 2;
	for (int i = 2; i < 15; i++) for (int j = 1; j < 15; j++) people_box[i][j] = people_box[i - 1][j] + people_box[i][j - 1];
	
	cin >> T;
	while (T--)
	{
	    cin >> a >> b;
	    cout << people_box[a][b] << '\n';
	}
}