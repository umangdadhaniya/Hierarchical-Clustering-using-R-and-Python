# load packages
import pandas as pd
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import LabelEncoder

# load data
insuranceData = pd.read_csv(r"C:\Dataset\Cluster\AutoInsurance.csv")
insData = insuranceData

# checking for na value
insuranceData.isna()
insuranceData.info()

# label encoding for -  ("Coverage","Education","Effective To Date","EmploymentStatus","Vehicle Class","Vehicle Size")
encoder = LabelEncoder()

insuranceData['Coverage']= encoder.fit_transform(insuranceData['Coverage'])
insuranceData['Education']= encoder.fit_transform(insuranceData['Education'])
insuranceData['Effective To Date']= encoder.fit_transform(insuranceData['Effective To Date'])
insuranceData['EmploymentStatus']= encoder.fit_transform(insuranceData['EmploymentStatus'])
insuranceData['Vehicle Class']= encoder.fit_transform(insuranceData['Vehicle Class'])
insuranceData['Vehicle Size']= encoder.fit_transform(insuranceData['Vehicle Size'])

# get dummy var data
listOfCol = ["State","Response","Gender","Location Code","Marital Status","Policy","Policy Type","Renew Offer Type","Sales Channel"]
dummyInsuranceData = pd.get_dummies(data= insuranceData,columns = listOfCol)

dummyInsuranceData.describe()

# standardize data
def colVariableStandardization(colVariable):
    return (colVariable - colVariable.mean()/colVariable.std())
stdData = colVariableStandardization(dummyInsuranceData.iloc[:, 1:])

# distance matrix - pairwise distance, dendrogram
gData = sch.linkage(stdData, method = 'complete', metric = 'euclidean')

sch.dendrogram(gData)

# agglomerative clustering

data = AgglomerativeClustering(n_clusters= 4, affinity='euclidean', linkage='complete').fit(gData)
data.labels_

clusterLabels = pd.Series(data.labels_)
clusterLabels

insData["insuranceCluster"] = clusterLabels

cols = insData.columns.tolist()
cols
cols = cols[-1:] + cols[:-1]
insData = insData[cols]

insData.to_csv("insuranceData.csv", encoding = "utf-8")

