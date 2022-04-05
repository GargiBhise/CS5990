import random
import networkx as nx

def watts_strogatz(prob, no_nodes, degree):
  '''
  prob = Probablity of Adding New Edge for Each New Node
  no_nodes = Number of Nodes in Graph
  degree = Highest Degree of Node in Graph
  '''
  lattice = make_ring_lattice(no_nodes, degree) # 'lattice' is a Graph Data Structure
  for node in range(lattice.order()): # '.order()' returns Number of Nodes in a Graph
    for i, j in lattice.edges(node): 
      if j <= i:
        continue
      k = random.randint(0, lattice.order()-1)
      if (i,k) in lattice.edges(i): 
        continue
      if i == k: 
        continue
      if (random.random() < prob):
        lattice.remove_edge(i,j)
        lattice.add_edge(i,k)
  print('Watts Strogatz Model Implemented (Iteration)')
  return lattice

def make_ring_lattice(no_nodes, no_edge):
  G = nx.Graph() # 'G' is a Graph Data Structure
  nodes = range(no_nodes) # 'nodes' is a List that contains Nodes of a Graph
  G.add_nodes_from(nodes) # Nodes are Added to Graph
  G.add_edges_from(adjacent_edges(nodes, no_edge//2)) # Edges based on Nodes and No. of Connections is added to Graph
  return G # Graph is Returned from the Function

def adjacent_edges(nodes, half_no_edge):
  lst_edges = []
  for index, value in enumerate(nodes):
      for j in range(index+1, index+half_no_edge+1): 
          t = nodes[j % len(nodes)] 
          lst_edges.append((value, t)) 
  return lst_edges
