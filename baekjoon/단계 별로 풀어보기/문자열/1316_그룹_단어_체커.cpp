#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	int result = 0, T, isit = 1;
	string word;
	
	char check;
	
	cin >> T;
	
	while(T--)
	{
	    bool alpha[26] = {false};
	    cin >> word;
	    check = word[0];
	    isit = 1;
	    alpha[(int)word[0] - 97] = true;
	    
	    for (int j = 0; j < word.length(); j++)
	    {
	        if (check != word[j])
	        {
	            if (alpha[(int)word[j] - 97])
	            {
	                isit = 0;
	                break;
	            }
	            alpha[(int)word[j] - 97] = true;
	            check = word[j];
	        }
	    }
	    result += isit;
	}
	cout << result;
}