import wget
import gzip
import shutil
import networkx as nx

from Watts_Strogatz_Model import watts_strogatz
from Barabasi_Albert_Model import barabasi_albert

url = 'https://snap.stanford.edu/data/facebook_combined.txt.gz'
wget.download(url, url.split('/')[-1])
with gzip.open(url.split('/')[-1], 'rb') as f_in:
    with open(url.split('/')[-1].split('.')[0]+'.txt', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

facebook_graph = nx.read_edgelist('facebook_combined.txt', nodetype=int)

size_facebook = facebook_graph.order()
avg_degree_facebook = round((float(facebook_graph.size())/size_facebook),5)
avg_path_length_facebook = round(nx.average_shortest_path_length(facebook_graph),5)
clustering_coeff_facebook = round(nx.average_clustering(facebook_graph),5)

facebook_watts_strogatz = watts_strogatz(0.1, len(facebook_graph), 22)
avg_path_length_facebook_watts_strogatz = round(nx.average_shortest_path_length(facebook_watts_strogatz),5)
clustering_coeff_facebook_watts_strogatz = round(nx.average_clustering(facebook_watts_strogatz),5)
b_vals = [0.01, 0.1, 0.5]
degrees = [20, 22, 24]
results = {}
for b in b_vals:
  for d in degrees:
    fws = watts_strogatz(b, len(facebook_graph), d)
    avg_path_length = round(nx.average_shortest_path_length(fws),5)
    clustering_coeff = round(nx.average_clustering(fws),5)
    results[(b,d)] = [avg_path_length, clustering_coeff]

facebook_barabasi_albert = barabasi_albert(len(facebook_graph), 2, 1)
avg_path_length_facebook_barabasi_albert = round(nx.average_shortest_path_length(facebook_barabasi_albert),5)
clustering_coeff_facebook_barabasi_albert = round(nx.average_clustering(facebook_barabasi_albert),5)
starts = [2, 5, 10]
degrees = [1, 2, 5] 
results = {}
for s in starts:
  for m in degrees:
    fba = barabasi_albert(len(facebook_graph), s, m)
    avg_path_length = round(nx.average_shortest_path_length(fba),5)
    clustering_coeff = round(nx.average_clustering(fba),5)
    results[(s, m)] = [avg_path_length, clustering_coeff]
