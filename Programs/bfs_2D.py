# Program to do bfs in 2-d matrix assuming you are provided wioth the start node and the
# only directions you can travel is up down left and right

from collections import deque

print("Enter size of the matrix:")
n, m = map(int, input().split())
visited = [[0 for i in range(m)] for i in range(n)]

# keeping track of every node from the root node
dist = [[0 for i in range(m)] for i in range(n)]


def isValid(node_x, node_y):

    if 0 <= node_x <= n-1 and 0 <= node_y <= m-1:
        if visited[node_x][node_y] == 0:
            return True
    else:
        return False


# level order traversal with respect to the root node
def bfs(root_x, root_y):
    visited[root_x][root_y] = 1
    
    q = deque()
    q.append([root_x, root_y])

    # up,right,down,left
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while len(q) > 0:
        node = q.popleft()
        for i in range(len(dx)):
            new_x = node[0] + dx[i]  
            new_y = node[1] + dy[i]  
            if isValid(new_x, new_y):
                visited[new_x][new_y] = 1
                # distance of child node = distance of parent node + 1
                dist[new_x][new_y] = dist[node[0]][node[1]] + 1
                # append the new nodes to the queue
                q.append([new_x, new_y])

print("Enter which node you want to act as the root node")
node, y = map(int, input().split())
bfs(node, y)

for i in range(0, n):
    print(" ".join(str(j) for j in dist[i][0:]))

