# load packages
import pandas as pd
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering

# load data
crimeData = pd.read_csv(r"C:\Dataset\Cluster\crime_data.csv")

# standardize data
def colVariableStandardization(colVariable):
    return (colVariable - colVariable.mean()/colVariable.std())
stdData = colVariableStandardization(crimeData.iloc[:, 1:])

stdData.describe()
stdData.info()

# distance matrix - pairwise distance, dendrogram
gData = sch.linkage(stdData, method = 'complete', metric = 'euclidean')

sch.dendrogram(gData)
# agglomerative clustering

data = AgglomerativeClustering(n_clusters= 4, affinity='euclidean', linkage='complete').fit(gData)
data.labels_

clusterLabels = pd.Series(data.labels_)
clusterLabels

crimeData["crimeCluster"] = clusterLabels

finalData = crimeData.iloc[:, [5,0,1,2,3,4]]

finalData.to_csv("crimeData", encoding = 'utf-8')
