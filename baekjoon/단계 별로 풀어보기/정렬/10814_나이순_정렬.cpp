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
	
	int N, age;
	string name;
	vector<tuple<int, int, string>> people;
	
	cin >> N;
	for (int order = 0; order < N; order++){
	    cin >> age >> name;
	    people.push_back(make_tuple(age, order, name));
	}
	
	sort(people.begin(), people.end());
	
	for (auto person : people) cout << get<0>(person) << " " << get<2>(person) << "\n";
}