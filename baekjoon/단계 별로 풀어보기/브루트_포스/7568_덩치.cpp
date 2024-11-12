#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;

int main()
{
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	int N, a, b;
	cin >> N;
	vector<int> result;
	vector<int> l1;
	vector<int> l2;
	
	for (int i = 0; i < N; i++){
	    cin >> a >> b;
	    l1.push_back(a);
	    l2.push_back(b);
	}
	
	for (int present = 0; present < N; present++){
	    int temp = 1;
	    for (int next = 0; next < N; next++){
	        if (l1[present] < l1[next] && l2[present] < l2[next]) temp++;
	    }
	    result.push_back(temp);
	}
	
	for (auto i : result) cout << i << " ";
}