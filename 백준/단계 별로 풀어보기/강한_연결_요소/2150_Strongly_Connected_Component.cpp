#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;

int dfs(int present, int &n, vector<int>& stack, vector<int>& dfsn, vector<int>& upper, vector<bool>& finished, vector< vector<int> >& final_scc_set, vector< vector<int> >& edge)
{
    stack.push_back(present);
    dfsn[present] = n;
    upper[present] = n;
    n++;
    
    for (auto next_vertex : edge[present]){
        if (finished[next_vertex]) continue;
        else if (dfsn[next_vertex] < 0){
            int temp_up = dfs(next_vertex, n, stack, dfsn, upper, finished, final_scc_set, edge);
            upper[present] = min(temp_up, upper[present]);
        }
        else upper[present] = min(upper[present], upper[next_vertex]);
    }
    
    if (upper[present] == dfsn[present]){
        int p = -1;
        vector<int> part_scc;
        
        while (p != present){
            p = stack.back();
            stack.pop_back();
            finished[p] = true;
            part_scc.push_back(p);
        }
        sort(part_scc.begin(), part_scc.end());
        final_scc_set.push_back(part_scc);
    }
    return upper[present];
}

int main()
{
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	
	//입력부
	int V, E, a, b;
	cin >> V >> E;
	
	vector< vector<int> > edge(V + 1, vector<int>(0, 0));
	for (int i = 0; i < E; i++){
	    cin >> a >> b;
	    edge[a].push_back(b);
	}
	
	//dfs 전처리
	vector<int> dfsn(V + 1, -1);
	vector<int> upper(V + 1, 0);
	vector<bool> finished(V + 1, false);
	vector<int> stack;
	vector< vector<int> > final_scc_set;
	int n = 1;
	
	for (int i = 1; i <= V; i++){
	    if (!finished[i]) dfs(i, n, stack, dfsn, upper, finished, final_scc_set, edge);
	}
	
	cout << final_scc_set.size() << '\n';

	sort(final_scc_set.begin(), final_scc_set.end());
	for (auto each : final_scc_set){
	    for (auto i : each) cout << i << " ";
	    cout << "-1\n";
	}
}