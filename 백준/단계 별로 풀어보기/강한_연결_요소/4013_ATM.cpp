#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <set>
#include <deque>
using namespace std;

int maxV = 500000, maxE = 500000;

//입력부 처리
vector<int> weight;
set<int> end_point;

//dfs 전처리
vector<int> dfsn(maxV + 1, -1);
vector<int> upper(maxV + 1, 0);
vector<vector<int>> edge(maxV + 1, vector<int>(0, 0));
vector<int> stack;
int n = 0;

//dfs 내 scc 전처리
vector<int> scc_weight;
vector<int> scc_end_point;
vector<int> element_locate(maxV + 1, -1);
int scc_count = 0;


int dfs(int present)
{
    stack.push_back(present);
    dfsn[present] = upper[present] = ++n;
    
    for (auto next_vertex : edge[present]){
        if (element_locate[next_vertex] != -1) continue;
        else if (dfsn[next_vertex] < 0) upper[present] = min(dfs(next_vertex), upper[present]);
        else upper[present] = min(upper[present], upper[next_vertex]);
    }
    
    if (upper[present] == dfsn[present]){
        int p = -1;
        int present_weight = 0;
        bool present_end = false;
        
        while (p != present){
            p = stack.back();
            stack.pop_back();
            present_weight += weight[p - 1];
            if (end_point.count(p)) present_end = true;
            element_locate[p] = scc_count;
        }
        scc_weight.push_back(present_weight);
        scc_end_point.push_back(present_end);
        scc_count++;
    }
    return upper[present];
}

int main()
{
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	
	//입력부
	int V, E, input1, input2;
	cin >> V >> E;
	
	for (int i = 0; i < E; i++){
	    cin >> input1 >> input2;
	    edge[input1].push_back(input2);
	}
	
	for (int i = 0; i < V; i++){
	    cin >> input1;
	    weight.push_back(input1);
	}
	
	int start, end_counter;
	cin >> start >> end_counter;
	
	for (int i = 0; i < end_counter; i++){
	    cin >> input1;
	    end_point.insert(input1);
	}
	
	dfs(start);
	
	//===================================
	//dfs 실행 후 scc 순회 전처리
	vector<vector<int>> scc_edge(scc_count, vector<int> (0, 0));
	vector<int> indegree(scc_count, 0);
	vector<int> scc_max(scc_count, 0);
	int MAX = 0;
	
	
	for (int start = 1; start <= V; start++){
	    if (element_locate[start] == -1) continue;
	    for (auto end : edge[start]){
	        int S = element_locate[start];
	        int E = element_locate[end];
	        
	        if (S != E && E != -1){
	            scc_edge[S].push_back(E);
	            indegree[E]++;
	        }
	    }
	}
	
	deque<int> que(1, scc_count - 1);
	scc_max[scc_count - 1] = scc_weight[scc_count - 1];
	
	while (!que.empty()){
	    int present_locate = que.front();
	    que.pop_front();
	    
	    if (scc_end_point[present_locate]) MAX = max(MAX, scc_max[present_locate]);
	    
	    for (auto next_vertex : scc_edge[present_locate]){
	        scc_max[next_vertex] = max(scc_max[next_vertex], scc_max[present_locate] + scc_weight[next_vertex]);
	        if (!--indegree[next_vertex]) que.push_back(next_vertex);
	    }
	}
	cout << MAX;
}