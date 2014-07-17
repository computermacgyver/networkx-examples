

#Intro to NetworkX by Scott A. Hale, GNU
#Reference at http://networkx.github.io/documentation/latest/reference/

import networkx as nx

g=nx.Graph() #A new (empty) undirected graph
g.add_node("Alan") #Add one new node
g.add_nodes_from(["Bob","Carol","Denise"])#Add three new nodes

#Nodes can have attributes
g.node["Alan"]["gender"]="M"
g.node["Bob"]["gender"]="M"
g.node["Carol"]["gender"]="F"
g.node["Denise"]["gender"]="F"

for n in g:
	print("{0} has gender {1}".format(n,g.node[n]["gender"]))
print()

#Interesting graphs have edges
g.add_edge("Alan","Bob") #Add one new edge

#Add two new edges
g.add_edges_from([["Carol","Denise"],["Carol","Bob"]])

#Edge attributes
g.edge["Alan"]["Bob"]["relationship"]="Friends"
g.edge["Carol"]["Denise"]["relationship"]="Friends"
g.edge["Carol"]["Bob"]["relationship"]="Married"

#New edge with an attribute
g.add_edges_from([["Carol","Alan",{"relationship":"Friends"}]])

for e in g.edges_iter():
	n1=e[0]
	n2=e[1]
	print("{0} and {1} are {2}".format(n1,n2,g.edge[n1][n2]["relationship"]))
print()

print("Nodes:",g.number_of_nodes())
print(g.nodes(data=True))
print()

print("Edges:",g.number_of_edges())
print(g.edges(data=True))
print()

#print(nx.info(g)) #Skip this

print("Density: {0}".format(nx.density(g)))
print("Connected componets: {0}".format(nx.number_connected_components(g)))
print()

print("Degree histogram: {0}".format(nx.degree_histogram(g)))
print("Betweenness Centrality {0}".format(nx.betweenness_centrality(g)))
print()

print("Clustering: {0}".format(nx.clustering(g)))
print("Bob's Clustering: {0}".format(nx.clustering(g, nodes=["Bob"])))
print()

#Save g to the file my_graph.graphml in graphml format
#prettyprint will make it nice for a human to read
nx.write_graphml(g,"my_graph.graphml",prettyprint=True)


#Layout g with the Fruchterman-Reingold force-directed
#algorithm and save the result to my_graph.png
#with_labels will label each node with its id
import matplotlib.pyplot as plt

nx.draw_spring(g,with_labels=True)
plt.savefig("my_graph.png")
plt.clf() #Clear plot

def print_top(lst,num=5):
	#Print the top num items of lst in decreasing order
	s=sorted(lst,key=lambda item: -lst[item])
	print("\tValue\tNode")
	for i in range(0,min(num,len(s))):
		print("{0}\t{1}\t{2}".format(i+1,lst[s[i]],s[i]))

n=3
print("Top nodes by clustering coefficients")
print_top(nx.clustering(g),num=n)
print("")

print("Top nodes by degree centrality (normalized 0-1)")
print_top(nx.degree_centrality(g),num=n)
print("")

print("Top nodes by betweenness centrality")
print_top(nx.betweenness_centrality(g),num=n)
print("")

print("Top nodes by eigenvector centrality")
print_top(nx.eigenvector_centrality(g),num=n)
print("")

