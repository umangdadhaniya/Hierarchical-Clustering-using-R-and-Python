# load packages
install.packages("readxl")
library(readxl)
install.packages("readr")
library(readr)

# load data
airlinePath <- "C:/Dataset/Cluster/EastWestAirlines.xlsx"
excel_sheets(path = airlinePath)
airlineData <- read_excel(path = airlinePath, sheet = "data")

# standardize data
stdAirlineData <- scale(airlineData[,-1])

summary(stdAirlineData)

# distance matrix - pairwise distance
distData <- dist(stdAirlineData, method = "euclidean")

clusterData <- hclust(distData, method = "complete")

# plot the data - Dendrogram
plot(clusterData, hang = -1)

# set huge k as data is very big
groupData <- cutree(clusterData, k = 100)

rect.hclust(clusterData, k = 100, border = 'red')

# creating final data
data <- as.matrix(groupData)
finalData <- data.frame(data, airlineData)

# write to file
write.csv(finalData, "airlineData.csv")
