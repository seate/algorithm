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
	
	string S;
	while (true){
	    getline(cin, S);
	    if (S == ".") break;
	    stack<bool> st;
	    bool isit = true;
	    
	    for (auto &s : S){
	        if (s == '(') st.push(true);
	        else if (s == ')'){
	            if (!st.empty() && st.top()) st.pop();
	            else{
	                isit = false;
	                break;
	            }
	        }
	        else if (s == '[') st.push(false);
	        else if (s == ']'){
	            if (!st.empty() && !st.top()) st.pop();
	            else{
	                isit = false;
	                break;
	            }
	        }
	    }
	    cout << ((isit && st.empty()) ? "yes" : "no") << "\n";
	}
}