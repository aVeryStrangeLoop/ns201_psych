library(ggplot2)
data <- read.csv("~/wsl_files/ns201_code/analysis/accuracies.csv")
data$abs_slope <- as.factor(data$abs_slope)
names(data)
data$accuracy <- data$accuracy/100.0
data_agg <- aggregate(x=data["accuracy"],by=list(slope=data$abs_slope,noise=data$noise),FUN=function(x) c(mn = mean(x), stdev = sd(x)))
data_agg <- do.call(data.frame,data_agg)
colnames(data_agg)[3] <- "mn"
colnames(data_agg)[4] <- "stdev"
names(data_agg)


p <- ggplot(data_agg[data_agg$slope==0.06,],aes(x=0.3-noise,y=mn,color="#000000")) + 
  geom_point() +
  geom_errorbar(aes(ymin=mn-stdev,ymax=mn+stdev))+ 
  theme_minimal()  +
  xlab("Noise (SD of Gaussian noise)") + ylab("Accuracy") + labs(color="mean slope")+
  scale_x_continuous(breaks = round(seq(0.0, 0.3, by = 0.03),1))+
  scale_y_continuous(breaks = round(seq(0.3, 1.0, by = 0.1),1))
p + theme(legend.position="none") + ylim(0.2,1.2)

library(quickpsy)
data_fit <- data <- read.csv("~/wsl_files/ns201_code/analysis/per_image.csv")
data_fit$slope <- as.factor(abs(data_fit$slope))
data_fit$noise <- 0.3-data_fit$noise
fit <-  quickpsy(data_fit, noise, correct, grouping = c("slope"),fun = logistic_fun,guess=0.5) 
plot(fit) + coord_cartesian(xlim=c(0,0.3)) + theme_minimal() + xlab("0.3-Noise (SD of Gaussian)") + ylab("Fractional Accuracy") + labs(color="Slope")
fit2 <-  quickpsy(data_fit, noise, correct, grouping = c("slope","exp_code"),fun = logistic_fun,guess=0.5) 

ths <- data.frame(fit["thresholds"])
ths$thresholds.threinf <- ths$thresholds.thre-ths$thresholds.threinf
ths$thresholds.thresup <- ths$thresholds.thresup-ths$thresholds.thre
ths$thresholds.thre <- 0.3 - ths$thresholds.thre

p <- ggplot(ths,aes(x=thresholds.slope,y=thresholds.thre,group=1)) + geom_point() + 
  geom_line() + theme_minimal() + 
  geom_errorbar(aes(ymin=thresholds.thre-thresholds.threinf,ymax=thresholds.thre+thresholds.thresup),width=0.1)
p + xlab("Slope") + ylab("Noise threshold")



data_fit2  <- read.csv("~/wsl_files/ns201_code/analysis/per_image.csv")
data_fit2$slope <- data_fit2$slope
data_fit2$noise <- 0.3-data_fit2$noise
data_fit2$type <- ifelse(data_fit2$slope > 0.0, "p", "n")
data_fit2$slope <- as.factor(abs(data_fit2$slope))
fit2 <-  quickpsy(data_fit2, noise, correct, grouping = c("slope","type"),fun = logistic_fun,guess=0.5) 
plot(fit2) + coord_cartesian(xlim=c(0,0.3)) + theme_minimal() + xlab("0.3-Noise (SD of Gaussian)") +
  ylab("Fractional Accuracy") + labs(color="Slope") + facet_grid(.~type)

ths2 <- data.frame(fit2["thresholds"])
ths2$thresholds.threinf <- ths2$thresholds.thre-ths2$thresholds.threinf
ths2$thresholds.thresup <- ths2$thresholds.thresup-ths2$thresholds.thre
ths2$thresholds.thre <- 0.3 - ths2$thresholds.thre
names(ths2)

p <- ggplot(ths2,aes(x=thresholds.slope,y=thresholds.thre,group=thresholds.type,color=thresholds.type)) + geom_point() + 
  geom_line() + theme_minimal() +
  geom_errorbar(aes(ymin=thresholds.thre-thresholds.threinf,ymax=thresholds.thre+thresholds.thresup,alpha=0.1),width=0.1)
p + xlab("Slope") + ylab("Noise threshold")  

