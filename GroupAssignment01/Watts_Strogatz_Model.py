import random
import networkx as nx

def adjacent_edges(nodes, halfk):
  lst_edges = []
  for index, value in enumerate(nodes):
      for j in range(index+1, index+halfk+1): 
          t = nodes[j % len(nodes)] 
          lst_edges.append((value, t)) 
  return lst_edges

def make_ring_lattice(n, k):
  G = nx.Graph()
  nodes = range(n)
  G.add_nodes_from(nodes)
  G.add_edges_from(adjacent_edges(nodes, k//2))
  return G

def decision(probability):
    return random.random() < probability

def watts_strogatz(b, v, c):
  lattice = make_ring_lattice(v, c)
  for node in range(lattice.order()):
    for i, j in lattice.edges(node):
      if j <= i:
        continue
      k = random.randint(0, lattice.order()-1)
      if (i,k) in lattice.edges(i): 
        continue
      if i == k: 
        continue
      if decision(b):
        lattice.remove_edge(i,j)
        lattice.add_edge(i,k)
  return lattice

