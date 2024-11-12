#include <iostream>
#include <vector>
#include <string>
#include <cstring>
using namespace std;

int main()
{
    cin.tie(NULL);
    cout.tie(NULL);
    ios_base::sync_with_stdio(false);
    
    int T;
	cin >> T;
	
	for (int i = 0; i < T; i ++)
	{
	    int result_score = 0;
	    int plus_score = 1;
	    char quiz[80];
	    cin >> quiz;
	    for (int j = 0; j < strlen(quiz); j++)
	    {
	        if (quiz[j] == 'O')
	        {
	            result_score += plus_score;
	            plus_score += 1;
	        }
	        else plus_score = 1;
	    }
	    cout << result_score << '\n';
	}
}