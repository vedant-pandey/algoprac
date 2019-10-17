from collections import defaultdict as ddict

class Graph :

  def __init__(self) :
    self.graph = ddict(list)

  def add_edge(self, u, v) :
    self.graph[u].append[v]

  def DFS_util(self, v, visited) :
    visited[v] = True
    print(v, end = ' ')

    for i in self.graph[v] :
      if visited[i] == False :
        self.DFS_util(i, visited)

  def DFS(self, v) :
    visited = [False] * (len(self.graph))

    self.DFS_util(v, visited)

  def BFS(self, s) :
    
    visited = [False] * (len(self.graph))
    queue = []
    queue.append(s)
    visited[s] = True

    while queue :
      s = queue.pop(0)
      print(s, end = ' ')

      for i in self.graph[s] :
        if visited[i] == False:
          queue.append(i)
          visited[i] = True

if __name__ == "__main__":
  b_or_d = int(input('1 - BFS \n2 - DFS\n\n'))

  if b_or_d == 2 :
    g1 = Graph()
    g1.add_edge(0, 1) 
    g1.add_edge(0, 2) 
    g1.add_edge(1, 2) 
    g1.add_edge(2, 0) 
    g1.add_edge(2, 3) 
    g1.add_edge(3, 3) 
    print("Following is DFS from (starting from vertex 2)") 
    g1.DFS(2)

  else :
    g2 = Graph() 
    g2.add_edge(0, 1) 
    g2.add_edge(0, 2) 
    g2.add_edge(1, 2) 
    g2.add_edge(2, 0) 
    g2.add_edge(2, 3) 
    g2.add_edge(3, 3) 
    print ("Following is Breadth First Traversal (starting from vertex 2)") 
    g2.BFS(2) 