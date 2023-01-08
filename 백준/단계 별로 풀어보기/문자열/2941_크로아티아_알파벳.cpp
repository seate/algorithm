#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	int idx;
	vector<string> croatia = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};
	string word;
	cin >> word;
	
	for (int i = 0 ; i < croatia.size(); i++)
	{
	    while (true)
	    {
	        idx = word.find(croatia[i]);
	        if (idx == string::npos) break;
	        word.replace(idx, croatia[i].length(), "*");
	    }
	}
	cout << word.length();
}