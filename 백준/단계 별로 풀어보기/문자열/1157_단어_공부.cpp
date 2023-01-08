#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
    cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	
    string word;
	int counter[26]{0,};
	
	cin >> word;
	transform(word.begin(), word.end(), word.begin(), ::toupper);
	
	for (int i = 0; i < word.length(); i++) counter[(int)word[i] - 65]++;
	
	int idx, M = *max_element(counter, counter + 26), c = 0;
	
	for (int i = 0; i < 26; i++)
	{
	    if (counter[i] == M)
	    {
	        c++;
	        idx = i;
	        if (1 < c) break;
	    }
	}
	
	if (1 < c) cout << "?";
	else cout << (char)(idx + 65);
}