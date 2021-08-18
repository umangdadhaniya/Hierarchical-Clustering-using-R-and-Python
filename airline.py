 # load packages
import pandas as pd
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering

# load data
airlinePath = "C:\Dataset\Cluster\EastWestAirlines.xlsx"
airlineData = pd.read_excel(airlinePath, sheet_name = "data")

# standardize data
stdAirlineData = airlineData.iloc[:, 1:]

def colVariableStandardization(colVariable):
    return (colVariable - colVariable.mean()/colVariable.std())
stdData = colVariableStandardization(stdAirlineData)

stdData.describe()
stdData.info()

# distance matrix - pairwise distance, dendrogram
gData = sch.linkage(stdData, method = 'complete', metric = 'euclidean')

sch.dendrogram(gData)

# agglomerative clustering

data = AgglomerativeClustering(n_clusters= 100, affinity='euclidean', linkage='complete').fit(gData)
data.labels_

clusterLabels = pd.Series(data.labels_)
clusterLabels

airlineData["airlineCluster"] = clusterLabels

finalData = airlineData.iloc[:, [12,0,1,2,3,4,5,6,7,8,9,10,11]]

finalData.to_csv("airlineData.csv", encoding = "utf-8")
