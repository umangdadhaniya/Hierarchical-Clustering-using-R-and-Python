# load packages
install.packages("readr")
library(readr)
install.packages("CatEncoders")
library(CatEncoders)
install.packages("fastDummies")
library(fastDummies)

# load data
insuranceData <- read_csv("C:/Dataset/Cluster/AutoInsurance.csv")
insDataCopy <- insuranceData

# checking for null data
sum(is.na(insDataCopy))

# label encoding for -  ("Coverage","Education","Effective To Date","EmploymentStatus","Vehicle Class","Vehicle Size")
lblCoverage <- LabelEncoder.fit(insuranceData$Coverage)
insDataCopy$Coverage<- transform(lblCoverage,insuranceData$Coverage)
# Education encoding
lblEducation <- LabelEncoder.fit(insuranceData$Education)
insDataCopy$Education<- transform(lblEducation,insuranceData$Education)
# Effective To Date encoding
lblDate <- LabelEncoder.fit(insuranceData$`Effective To Date`)
insDataCopy$`Effective To Date`<- transform(lblDate,insuranceData$`Effective To Date`)
# EmploymentStatus encoding
lblEmploymentStatus <- LabelEncoder.fit(insuranceData$EmploymentStatus)
insDataCopy$EmploymentStatus<- transform(lblEmploymentStatus,insuranceData$EmploymentStatus)
# Vehicle Class encoding
lblClass <- LabelEncoder.fit(insuranceData$`Vehicle Class`)
insDataCopy$`Vehicle Class`<- transform(lblClass,insuranceData$`Vehicle Class`)
# Vehicle Size encoding
lblSize <- LabelEncoder.fit(insuranceData$`Vehicle Size`)
insDataCopy$`Vehicle Size`<- transform(lblSize,insuranceData$`Vehicle Size`)



#one hot encoding
processedInsData <- dummy_cols(insDataCopy, 
                                 select_columns = c("State","Response","Gender","Location Code","Marital Status","Policy","Policy Type","Renew Offer Type","Sales Channel"), 
                                 remove_first_dummy =  TRUE, 
                                 remove_most_frequent_dummy = FALSE, 
                                 remove_selected_columns = TRUE)

summary(processedInsData)
# take 5000 rows only
iData <- processedInsData[5000,]
# distance matrix
distInsData <- dist(processedInsData, method = "euclidean")

clusterData <- hclust(distInsData, method = "complete")

# plot the data - Dendrogram
plot(clusterData, hang = -1)

groupData <- cutree(clusterData, k = 4)

rect.hclust(clusterData, k = 4, border = 'red')

# creating final data
data <- as.matrix(groupData)
finalData <- data.frame(data, insuranceData)

# write to file
write.csv(finalData, "insurance.csv")

aggregate(finalData, list(finalData$data), mean)
# so group 3 gives maximum premium while group 1 gives minimum premium
