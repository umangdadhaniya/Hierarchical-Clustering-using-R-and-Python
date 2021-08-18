# load packages
install.packages("readxl")
library(readxl)
install.packages("readr")
library(readr)

# load data
crimeData <- read_csv("C:/Dataset/Cluster/crime_data.csv")

sum(is.na(crimeData))

outliers <- boxplot(crimeData$Murder)
View(outliers$out)

# standardize data
stdCrimData <- scale(crimeData[, -1])

# distance matric
distCrimeData <- dist(stdCrimData, method = "euclidean")

clusterCrimeData <- hclust(distCrimeData, method = "complete")

# plot crime data
plot(clusterCrimeData, hang = -1)

groupCrimeData <- cutree(clusterCrimeData, k = 4)

rect.hclust(clusterCrimeData, k = 4, border = 'red')

# get final data 
data <- as.matrix(groupCrimeData)
finalData <- data.frame(data, crimeData)

# write to file
write.csv(finalData, "crimeData.csv")
