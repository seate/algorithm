#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	int locate[26];
	string word;
	fill_n(locate, 26, -1);
	
	cin >> word;
	
	for (int i = 0; i < word.length(); i++)
	{
	    if (locate[(word[i] - '0' - 49)] == -1) locate[(word[i] - '0' - 49)] = i;
	}
	
	for (int i = 0; i < 26; i++) cout << locate[i] << ' ';
}