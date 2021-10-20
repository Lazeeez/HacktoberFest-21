package competitiveProgramming;

import java.util.*;

public class GenericGraph <T> {

	private HashMap<T, LinkedList<T>> map;
	private List<T> dfs_vis = new ArrayList<>();
	
	public GenericGraph() {
		map = new HashMap<>();
	}
	
	public void addVertex(T label) {
		map.put(label, new LinkedList<T>());
	}
	
	public void addEdge(T init, T fin, boolean undirected) {
		if(!map.containsKey(init)) {
			addVertex(init);
		}
		
		if(!map.containsKey(fin)) {
			addVertex(fin);
		}
		
		map.get(init).add(fin);
		
		if(undirected) {
			map.get(fin).add(init);
		}
	}
	
	public boolean hasVertex(T v) {
		return map.containsKey(v);
	}
	
	public boolean hasEdge(T src, T des) {
		return map.get(src).contains(des);
	}
	
	public int numVertices() {
		return map.keySet().size();
	}
	
	
	@Override
	public String toString() {
		
		String s = "";
		
		for(T i: map.keySet()) {
			s += i.toString() + ":";
			
			for(T j: map.get(i)) {
				s += j.toString() + " ";
			}
			s += "\n";
		}
		
		return s;
	}
	
	public List<T> dfs(T n) {
		
		dfs_vis.add(n);
		
		for(T i : map.get(n)) {
			if(!dfs_vis.contains(i)) {
				dfs(i);
			}
		}
		return dfs_vis;
	}
	
	public HashMap<T, Integer> bfs(T n) {
		int v = numVertices();
		Queue<T> q = new LinkedList<>();
		ArrayList<T> vis = new ArrayList<>();
		HashMap<T, Integer> dis = new HashMap<>();
		
		q.add(n);
		vis.add(n);
		dis.put(n, 0);
		
		while(!q.isEmpty()) {
			T cur = q.poll();
			
			for(T i : map.get(cur)) {
				if(!vis.contains(i)) {
					vis.add(i);
					dis.put(i, dis.get(cur) + 1);
					q.add(i);
				}
			}
		}
		
		return dis;
	}
	
	public boolean hasPath(T src, T des) {
		ArrayList<T> dfs_list = (ArrayList<T>) dfs(src);
		
		if(dfs_list.contains(des)) {
			return true;
		} else {
			return false;
		}
		
	}

}