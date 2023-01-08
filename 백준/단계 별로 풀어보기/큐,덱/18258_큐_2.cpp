#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <tuple>
#include <queue>
using namespace std;

int main()
{
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	int T, num;
	cin >> T;
	string str;
	queue<int> q;
	
	while (T--){
	    cin >> str;
	    char c = str[0];
	    
	    if (c == 'p'){
	    	if (str[1] == 'u'){
	    		cin >> num;
	    		q.push(num);
	    	}
	    	else{
	    		if (q.empty()) cout << "-1\n";
	    		else{
	    			cout << q.front() << "\n";
	    			q.pop();
	    		}
	    	}
	    }
	    else if (c == 's') cout << q.size() << "\n";
	    else if (c == 'e') cout << q.empty() << "\n";
	    else if (q.empty()) cout << "-1\n";
	    else if (c == 'f') cout << q.front() << "\n";
	    else cout << q.back() << "\n";
	}
}