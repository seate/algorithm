#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	int T, repeat;
	string word;
	cin >> T;
	
	while (T--)
	{
	    cin >> repeat >> word;
	    for (int i = 0; i < word.length(); i++)
	    {
	        for (int j = 0; j < repeat; j++) cout << word[i];
	    }
	    cout << '\n';
	}
}