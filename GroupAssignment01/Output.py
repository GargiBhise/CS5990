import pandas as pd

from Main import size_facebook,avg_degree_facebook,avg_path_length_facebook,clustering_coeff_facebook,avg_path_length_facebook_watts_strogatz,clustering_coeff_facebook_watts_strogatz,avg_path_length_facebook_barabasi_albert,clustering_coeff_facebook_barabasi_albert

Output = {}

Output['Original Network'] = {'Size': size_facebook, 'Average Degree': avg_degree_facebook, 'Average Path Length': avg_path_length_facebook, 'Clustering Coefficient': clustering_coeff_facebook}
Output['Watts-Strogatz'] = {'Average Path Length': avg_path_length_facebook_watts_strogatz, 'Clustering Coefficient': clustering_coeff_facebook_watts_strogatz}
Output['Barabasi-Albert'] = {'Average Path Length': avg_path_length_facebook_barabasi_albert, 'Clustering Coefficient': clustering_coeff_facebook_barabasi_albert}

Output = pd.DataFrame.from_dict(Output)

Output.to_csv('Output.csv')
