
graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visited = []
znach = []

def bfs(visited, graph, node):
    global znach
    visited.append(node)
    znach.append(node)
    while znach:
        s = znach.pop(0)
        print (s, end = " ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                znach.append(neighbour)
bfs(visited, graph, 'B')