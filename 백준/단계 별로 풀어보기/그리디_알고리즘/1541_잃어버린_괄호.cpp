#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <tuple>
#include <sstream>
using namespace std;

//DECO*27 - 안드로이드 걸 feat. 하츠네 미쿠

vector<string> split(string &input, char split_criteria = ' '){
    vector<string> answer;
    stringstream ss(input);
    string temp;
    
    while (getline(ss, temp, split_criteria)) answer.push_back(temp);
    
    return answer;
}

int sum(vector<int> &arr){
    int S = 0;
    for (auto &s : arr) S += s;
    return S;
}

int main()
{
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	string original_formula;
	cin >> original_formula;
	
	vector<string> splited_by_minus = split(original_formula, '-');
	vector<vector<string>> splited_by_both;
	for (auto &str : splited_by_minus) splited_by_both.push_back(split(str, '+'));
	
	int result = 0;
	for (auto &i : splited_by_both[0]) result += stoi(i);
	result *= 2;
	
	for (auto &i : splited_by_both){
		for (auto &j : i) result -= stoi(j);
	}
	
	cout << result;
}