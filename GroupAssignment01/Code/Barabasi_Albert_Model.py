import random
import networkx as nx

def barabasi_albert(n, m0, m):
  '''
  m0 = no. of nodes initialised before adding new node
  n = number of nodes
  m = degree of node with highest degree
  '''
  g = nx.path_graph(m0)
  for new_node in range(m0, n):
    g.add_node(new_node)
    new_edges = []
    for _ in range(m):
      degrees = nx.degree(g)
      total = sum([degree for node,degree in degrees])
      nodes = [n for n in g.nodes()]
      probs = [degrees[node]/total for node in g.nodes()]
      element = random.choices(nodes[:-1], weights = probs[:-1], k = 1)
      g.add_edge(new_node, element[0])
      new_edges.append((new_node, element[0]))
  print('Barbasi Albert Model Implemented (Iteration)')
  return g
