library(ggplot2)
data <- read.csv("~/wsl_files/ns201_code/analysis/thresholds.csv")

data$thresholds.thre <- 0.3-data$thresholds.thre
p <- ggplot(data[data$thresholds.thre>0 & data$thresholds.thre<0.3,],aes(x=thresholds.thre,fill=thresholds.slope)) + geom_histogram(color="#000000",bins=8) + facet_grid(thresholds.slope~.)
p + theme_minimal() + xlab("Noise Threshold") + ylab("Count") + theme(legend.position = "none")

sd(data[data$thresholds.thre>0 & data$thresholds.thre<0.3 & data$thresholds.slope==0.02,]$thresholds.thre)
sd(data[data$thresholds.thre>0 & data$thresholds.thre<0.3 & data$thresholds.slope==0.04,]$thresholds.thre)
sd(data[data$thresholds.thre>0 & data$thresholds.thre<0.3 & data$thresholds.slope==0.06,]$thresholds.thre)
