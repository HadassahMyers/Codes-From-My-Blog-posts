def make_link(g,node1,node2):
	if node1 not in G:
		G[node1]={}
	(G[node1])[node2]=1
	if node2 not in G:
		G[node2]={}
	(G[node2])[node1]=1

G={}
connections = [('A','B'),('A','C'),('A','E'),('B','D'),('B','F'),('C','G'),('E','F')]
for x,y in connections:make_link(G,x,y)

print G
def dfs(G,node,traversed):
	traversed[node]=True
	#print "traversal:"+ node 
	for neighbour_nodes in G[node]:
		if neighbour_nodes not in traversed:
			dfs(G,neighbour_nodes,traversed)
def start_traversal(G):
	traversed = {}
	for node in G.keys():
		if node not in traversed:
			dfs(G,node,traversed);
start_traversal(G)

