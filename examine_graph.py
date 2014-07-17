import networkx as nx
import sys

if len(sys.argv)!=2:
	print("You must supply a graphml file as the argument.")
	quit()

g=nx.read_graphml(sys.argv[1])

def print_top(lst,num=5):
	#Print the top num items of lst in decreasing order
	s=sorted(lst,key=lambda item: -lst[item])
	print("\tValue\tNode")
	for i in range(0,min(num,len(s))):
		print("{0}\t{1}\t{2}".format(i+1,lst[s[i]],s[i]))


print("Nodes: {0}".format(g.number_of_nodes()))
print("")

print("Edges: {0}".format(g.number_of_edges()))
print("")

print(nx.info(g))
print("")

print("Density: {0}".format(nx.density(g)))

if nx.is_directed(g):
	print("Strongly connected components: {0}".format(nx.number_strongly_connected_components(g)))
	print("Weakly connected components: {0}".format(nx.number_weakly_connected_components(g)))

	largest_wcc=0
	for component in nx.weakly_connected_components(g):
		if largest_wcc<len(component):
			largest_wcc=len(component)
	print("Size of largest weakly connected component: {0}".format(largest_wcc))

else:
	print("Connected componets:",nx.number_connected_components(g))#Not implemented for directed graphs
	largest_comp=0
	for component in nx.connected_components(g):
		if largest_comp<len(component):
			largest_comp=len(component)
	print("Size of largest connected component: {0}".format(largest_comp))

print("")

n=5
#print("Top nodes by clustering coefficients")
#print_top(nx.clustering(g),num=n)
#print()

print("Top nodes by degree centrality (normalized 0-1)")
print_top(nx.degree_centrality(g),num=n)
print("")

if nx.is_directed(g):
	print("Top nodes by *in* degree centrality (normalized 0-1)")
	print_top(nx.in_degree_centrality(g),num=n)
	print("")


	print("Top nodes by *out* degree centrality (normalized 0-1)")
	print_top(nx.out_degree_centrality(g),num=n)
	print("")

print("Top nodes by page rank")
print_top(nx.pagerank(g),num=n)
print("")

if nx.number_of_nodes(g)<=500:
	#Betweenness centrality is expensive. Look at the approximation methods
	print("Top nodes by betweenness centrality")
	print_top(nx.betweenness_centrality(g),num=n)
	print()

print("Top nodes by eigenvector centrality")
print_top(nx.eigenvector_centrality(g),num=n)
print("")



#Layout g with the Fruchterman-Reingold force-directed
#algorithm and save the result to my_graph.png
#with_labels will label each node with its id
import matplotlib.pyplot as plt
#See http://matplotlib.org/users/pyplot_tutorial.html

nx.draw_spring(g,with_labels=True)
plt.savefig("my_graph.png")
plt.clf() #Clear plot

