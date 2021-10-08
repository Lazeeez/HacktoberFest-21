#include <bits/stdc++.h>
using namespace std;

//Using BFS Algorithm
//Intuition- indegree zero nodes wont have any edges so they are placed before. 
//indegree is being reduced as zero indegree nodes where taken beforehand.

class Solution
{
	public:
	//Function to return list containing vertices in Topological order. 
	//BFS Algo is used
	vector<int> topoSort(int V, vector<int> adj[]) 
	{
	    queue<int>q;
	    vector<int>indegree(V,0);
	    for(int i=0;i<V;i++)
	    {
	        for(auto it:adj[i])
	        indegree[it]++;
	    }
	    for(int i=0;i<V;i++)
	    {
	        if(indegree[i]==0)
	        q.push(i);
	    }
	    vector<int>topo;
	    while(!q.empty())
	    {
	        int node=q.front();
	        q.pop();
	        topo.push_back(node);
	        for(auto it:adj[node])
	        {
	            indegree[it]--;
	            if(indegree[it]==0)
	            q.push(it);
	        }
	    }
	    return topo;
	}
};

int check(int V, vector <int> &res, vector<int> adj[]) {
    vector<int> map(V, -1);
    for (int i = 0; i < V; i++) {
        map[res[i]] = i;
    }
    for (int i = 0; i < V; i++) {
        for (int v : adj[i]) {
            if (map[i] > map[v]) return 0;
        }
    }
    return 1;
}

int main() {
    int T;
    cin >> T;
    while (T--) {
        int N, E;
        cin >> E >> N;
        int u, v;

        vector<int> adj[N];

        for (int i = 0; i < E; i++) {
            cin >> u >> v;
            adj[u].push_back(v);
        }
        
        Solution obj;
        vector <int> res = obj.topoSort(N, adj);

        cout << check(N, res, adj) << endl;
    }
    
    return 0;
} 

//DFS Algorithm for topo sort
/*
void topoDFS(int node,vector<int>&vis,stack<int>&s,vector<int>adj[])
    {
        vis[node]=1;
        for(auto it:adj[node])
        {
            if(!vis[it])
            topoDFS(it,vis,s,adj);
        }
        s.push(node);
    }
vector<int> topoSort(int V, vector<int> adj[]) 
	{
	    stack<int>s;
	    vector<int>vis(V,0);
	    
	    for(int i=0;i<V;i++)
	    {
	        if(!vis[i])
	        topoDFS(i,vis,s,adj);
	    }
	    vector<int>topo;
	    while(!s.empty())
	    {
	        topo.push_back(s.top());
	        s.pop();
	    }
	    return topo;
	}
*/