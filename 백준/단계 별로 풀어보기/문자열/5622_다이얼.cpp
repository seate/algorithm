#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	int result = 0;
	string word;
	cin >> word;
	
	for (int i = 0; i < word.length(); i++)
	{
	    int I = (int)(word[i]) - 65;
	    if (I < 15) result += (I / 3 + 3);
	    else if (I < 19) result += 8;
	    else if (I < 22) result += 9;
	    else result += 10;
	}
	cout << result;
}