library(ggplot2)
data <- read.csv("~/wsl_files/ns201_code/analysis/accuracies.csv")
data$abs_slope <- as.factor(data$abs_slope)

data_agg <- aggregate(x=data["accuracy"],by=list(slope=data$abs_slope,noise=data$noise),FUN=function(x) c(mn = mean(x), stdev = sd(x)))
data_agg <- do.call(data.frame,data_agg)
colnames(data_agg)[3] <- "mn"
colnames(data_agg)[4] <- "stdev"
names(data_agg)

p <- ggplot(data_agg,aes(x=noise,y=mn,color=slope)) + 
  geom_point(position=position_dodge(.02)) +
  geom_errorbar(aes(ymin=mn-stdev,ymax=mn+stdev),width=0,position=position_dodge(.02))+ 
  theme_minimal() + scale_x_reverse() +
  xlab("Noise (SD of Gaussian noise)") + ylab("Accuracy") + labs(color="mean slope")
p + coord_cartesian(ylim=c(0, 100))

