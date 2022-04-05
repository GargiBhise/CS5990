import wget
import gzip
import shutil
import networkx as nx

from Watts_Strogatz_Model import watts_strogatz
from Barabasi_Albert_Model import barabasi_albert

url = 'https://snap.stanford.edu/data/facebook_combined.txt.gz'
# Download and Save Dataset
wget.download(url, url.split('/')[-1])
print('\nDataset Downloaded')
# Extracting '.gz' file and saving '.txt' Dataset
with gzip.open(url.split('/')[-1], 'rb') as f_in:
    with open(url.split('/')[-1].split('.')[0]+'.txt', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
print('Dataset Extracted and Saved')

# Creating Graph Data Structure from Dataset using NetworkX Library
facebook_graph = nx.read_edgelist('facebook_combined.txt', nodetype=int)
size_facebook = facebook_graph.order() # Number of Nodes in Graph
avg_degree_facebook = round((float(facebook_graph.size())/size_facebook),5) # Average Degree of Graph
avg_path_length_facebook = round(nx.average_shortest_path_length(facebook_graph),5) 
clustering_coeff_facebook = round(nx.average_clustering(facebook_graph),5) # Clustering Coefficient of Graph
results_networkx = {}
results_networkx['1'] = [size_facebook,avg_degree_facebook,avg_path_length_facebook,clustering_coeff_facebook]
print('Results from NetworkX Library Obtained')

prob_vals = [0.05, 0.25, 0.8] # List of Probablities of Adding New Edge with Node of HIghest Degree
lst_degrees = [25, 32, 45] # List of Highest Degree in a Graph
results_watts_strogatz = {}
iter = 1
for p in prob_vals:
  for d in lst_degrees:
    # Graph (Ring Lattice) created through Dataset using Watts Strogatz Model
    facebook_watts = watts_strogatz(p, len(facebook_graph), d) 
    # Average Path Length of Graph Created using Watts Strogatz Model (Rounded Off to 5 Decimal Places)
    avg_path_length = round(nx.average_shortest_path_length(facebook_watts),5) 
    # Clustering Coefficient of Graph Created using Watts Strogatz Model (Rounded Off to 5 Decimal Places)
    clustering_coeff = round(nx.average_clustering(facebook_watts),5)
    # A Dictionary is Created with set of Values of 'Average Path Length' and 'Clustering Coefficient' obtained through multiple Probablity and Degree Values 
    results_watts_strogatz[iter] = [iter,p,d,avg_path_length,clustering_coeff] # Storing all Values for Further Analysis
    iter += 1
print('Results from All Iterations of Watts Strogatz Obtained')

orig_nodes = [3, 5, 15] # No. of Nodes Initialised Before Adding New Node
degrees = [2, 4, 10] # List of Highest Degree in a Graph
results_barbasi_albert = {}
iter = 1
for s in orig_nodes:
  for d in degrees:
    # Graph (Path Graph) created through Dataset using Barbasi Albert Model
    facebook_barbasi = barabasi_albert(len(facebook_graph), s, d)
    # Average Path Length of Graph Created using Barbasi Albert Model (Rounded Off to 5 Decimal Places)
    avg_path_length = round(nx.average_shortest_path_length(facebook_barbasi),5)
    # Clustering Coefficient of Graph Created using Watts Barbasi Albert Model (Rounded Off to 5 Decimal Places)
    clustering_coeff = round(nx.average_clustering(facebook_barbasi),5)
    # A Dictionary is Created with set of Values of 'Average Path Length' and 'Clustering Coefficient' obtained through multiple Probablity and Degree Values 
    results_barbasi_albert[iter] = [iter,s,d,avg_path_length, clustering_coeff] # Storing all Values for Further Analysis
    iter += 1
print('Results from All Iterations of Barbasi Albert Model Obtained')
