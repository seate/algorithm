#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	int counter = 1;
	string str;
    getline(cin, str);
    
    for (int i = 0; i < str.length(); i++)
    {
        if (str[i] == ' ') counter++;
    }
    if (str[0] == ' ') counter--;
    if (str[str.length() - 1] == ' ') counter--;
    
	cout << counter;
}