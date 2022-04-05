import pandas as pd
from Main import results_networkx,results_watts_strogatz,results_barbasi_albert
print('Results from All Files Obtained for Exporting')

Output_NX = pd.DataFrame.from_dict(results_networkx).T
Output_NX.columns = ['Size','Average Degree', 'Average Path Length', 'Clustering Coefficient']
Output_NX.to_csv('../Outputs/Output_NX.csv',index=False)
print('Results from NetworkX Library Exported')

Output_WS = pd.DataFrame.from_dict(results_watts_strogatz).T
Output_WS.columns = ['Iteration','Probablity', 'Highest Degree', 'Avg Path Length', 'Clustering Coeff']
Output_WS.to_csv('../Outputs/Output_WS.csv',index=False)
print('Results from Watts Strogatz Exported')

Output_BA = pd.DataFrame.from_dict(results_barbasi_albert).T
Output_BA.columns = ['Iteration','Initialised Nodes', 'Highest Degree', 'Avg Path Length', 'Clustering Coeff']
Output_BA.to_csv('../Outputs/Output_BA.csv',index=False)
print('Results from Barbasi Albert Model Exported')

print('Thank You!')

