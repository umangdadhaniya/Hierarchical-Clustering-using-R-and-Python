# load packages
install.packages("readxl")
library(readxl)
install.packages("readr")
library(readr)
# load cluster package for daisy function
install.packages("cluster")
library(cluster)
install.packages("fastDummies")
library(fastDummies)

# load data
telecomData <- read_excel("C:/Dataset/Cluster/Telco_customer_churn.xlsx")

# checking for null data
sum(is.na(telecomData))

# avoid unwanted data cols
updatedTelecomData <- telecomData[,-c(2,3,4,5,6,8,10,11,12,13,14,15,16,17,18,19,20,21,22)]

# create dummy data 
processedTelecomData <- dummy_cols(updatedTelecomData, 
                              select_columns = c("Offer","Paperless Billing","Payment Method"), 
                              remove_first_dummy =  TRUE, 
                              remove_most_frequent_dummy = FALSE, 
                              remove_selected_columns = TRUE)

summary(processedTelecomData)
# distance matrix
distTelecomData <- dist(processedTelecomData, method = "euclidean")

clusterData <- hclust(distTelecomData, method = "complete")

# plot the data - Dendrogram
plot(clusterData, hang = -1)

groupData <- cutree(clusterData, k = 4)

rect.hclust(clusterData, k = 4, border = 'red')

# creating final data
data <- as.matrix(groupData)
finalData <- data.frame(data, updatedTelecomData)

# write to file
write.csv(finalData, "telecom.csv")

aggregate(finalData, list(finalData$data), mean)
# so group 4 gives maximum business while group 1 gives minimum n=business
