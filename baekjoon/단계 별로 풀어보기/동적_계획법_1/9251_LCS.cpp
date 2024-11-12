#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <tuple>
using namespace std;

int main()
{
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	string word1;
	string word2;
	cin >> word1 >> word2;
	
	vector<vector<int>> LCS(word2.size() + 1, vector<int>(word1.size() + 1));
	
	for (int i = 1; i <= word2.size(); i++){
	    for (int j = 1; j <= word1.size(); j++){
	        if (word1[j - 1] == word2[i - 1]) LCS[i][j] = LCS[i - 1][j - 1] + 1;
	        else LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1]);
	    }
	}
	
	cout << LCS[word2.size()][word1.size()];
}