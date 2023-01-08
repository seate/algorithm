#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <tuple>
#include <stack>
using namespace std;

int main()
{
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	stack<int> st;
	int T, num;
	cin >> T;
	string command;
	
	while (T--){
	    cin >> command;
	    
	    if (command[0] == 'p'){
	        if (command[1] == 'u'){
	            cin >> num;
	            st.push(num);
	        }
	        else if (st.empty()) cout << "-1\n";
	        else{
	            cout << st.top() << "\n";
	            st.pop();
	        }
	    }
	    
	    else if (command[0] == 's') cout << st.size() << "\n";
	    else if (command[0] == 'e') cout << st.empty() << "\n";
	    else if (st.empty()) cout << "-1\n";
	    else{
	        cout << st.top() << "\n";
	    }
	}
}