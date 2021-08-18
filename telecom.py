# load packages
import pandas as pd
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering

# load data
telecomData = pd.read_excel(r"C:\Dataset\Cluster\Telco_customer_churn.xlsx")

# checking for na value
telecomData.isna()
telecomData.describe()
telecomData.info()

# avoid unwanted data cols
updatedTelecomData = telecomData.drop(columns = ["Count","Quarter","Referred a Friend","Number of Referrals","Tenure in Months","Phone Service","Multiple Lines","Internet Service","Internet Type","Avg Monthly GB Download","Online Security","Online Backup","Device Protection Plan","Premium Tech Support","Streaming TV","Streaming Movies","Streaming Music","Unlimited Data","Contract"], axis = 1)

# get dummy var data
listOfCol = ["Offer","Paperless Billing","Payment Method"]
dummyTelecomData = pd.get_dummies(data= updatedTelecomData,columns = listOfCol)

dummyTelecomData.describe()

# standardize data
def colVariableStandardization(colVariable):
    return (colVariable - colVariable.mean()/colVariable.std())
stdData = colVariableStandardization(dummyTelecomData.iloc[:, 1:])

# distance matrix - pairwise distance, dendrogram
gData = sch.linkage(stdData, method = 'complete', metric = 'euclidean')

sch.dendrogram(gData)

# agglomerative clustering

data = AgglomerativeClustering(n_clusters= 4, affinity='euclidean', linkage='complete').fit(gData)
data.labels_

clusterLabels = pd.Series(data.labels_)
clusterLabels

telecomData["telecomCluster"] = clusterLabels

cols = telecomData.columns.tolist()
cols
cols = cols[-1:] + cols[:-1]
telecomData = telecomData[cols]
finalData = telecomData

finalData.to_csv("telecomData", encoding = 'utf-8')
