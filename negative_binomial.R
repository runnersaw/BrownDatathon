library(readxl)
library(MASS)
library(ggplot2)

dataset <- read_excel('gtd_94to15_aggregated.xlsx')

# Adds Freq of each (country_code, iyear) group
terror_freq <- data.frame(table(dataset$country_code, dataset$iyear))
dataset <- merge(x = dataset, y = terror_freq,
      by.x =c("country_code", "iyear"), by.y=c("Var1", "Var2"),  all.x = TRUE)

workingdata <- dataset[c("Freq",
                         "country_code_origin",
                         "iyear",
                         "Recent Conflict",
                         "rgdpe",
                         "polity",
                         "pop")]

workingdata$logpop <- log(workingdata$pop)
workingdata$logrgdpe <- log(workingdata$rgdpe)

workingdata = subset(workingdata, select = -c(pop, rgdpe))

# Impute NAs to Means
for(i in 1:ncol(workingdata)){
  workingdata[is.na(workingdata[,i]), i] <- lapply(workingdata[,i], mean, na.rm = FALSE)
}

nrow(workingdata)
workingdata <- unique(workingdata[complete.cases(workingdata),])
nrow(workingdata)
# filter outliers...
workingdata <- workingdata[workingdata$Freq < 500,]




ggplot(workingdata, aes(x=Freq)) +
  geom_histogram(binwidth=.5, colour="black", fill="white") +
  geom_vline(aes(xintercept=mean(Freq, na.rm=T)),   # Ignore NA values for mean
             color="red", linetype="dashed", size=1)
ggplot(workingdata, aes(x=`Recent Conflict`)) +
  geom_histogram(binwidth=.5, colour="black", fill="white") +
  geom_vline(aes(xintercept=mean(`Recent Conflict`, na.rm=T)),   # Ignore NA values for mean
             color="red", linetype="dashed", size=1)
ggplot(workingdata, aes(x=logrgdpe)) +
  geom_histogram(binwidth=0.5, colour="black", fill="white") +
  geom_vline(aes(xintercept=mean(logrgdpe, na.rm=T)),   # Ignore NA values for mean
             color="red", linetype="dashed", size=1)
ggplot(workingdata, aes(x=polity)) +
  geom_histogram(binwidth=.5, colour="black", fill="white") +
  geom_vline(aes(xintercept=mean(polity, na.rm=T)),   # Ignore NA values for mean
             color="red", linetype="dashed", size=1)
ggplot(workingdata, aes(x=logpop)) +
  geom_histogram(binwidth=.5, colour="black", fill="white") +
  geom_vline(aes(xintercept=mean(logpop, na.rm=T)),   # Ignore NA values for mean
             color="red", linetype="dashed", size=1)

n = 209
mean(workingdata$Freq)
var(workingdata$Freq)
data.nb = data.frame(Trt = c(rep("Recent Conflict", n),
                             rep("logrgpde", n),
                             rep("polity", n),
                             rep("logpop", n)),
                     Response = Freq)
# negative binomial
model <-glm.nb(
  Freq~`Recent Conflict`+logrgdpe+polity+logpop,
  workingdata, link=log)

# poisson
model <-glm(
  Freq~`Recent Conflict`+logrgdpe+polity+logpop,
  workingdata, family=poisson)

# model <- glm.nb(Response ~ Trt, data.nb)
summary(model)

# incidence rate ratios, used in the paper
exp(coef(model))
1 - pchisq(summary(model)$deviance, 
           summary(model)$df.residual
)


res <- data.frame(cbind(
Mean = predict(model, newdata = workingdata[c("Recent Conflict","logrgdpe", "polity", "logpop")], type ="response"),
SE = predict(model, newdata = workingdata[c("Recent Conflict","logrgdpe", "polity", "logpop")], type="response", se.fit = T)$se.fit
))

mean(res$Mean)
var(res$Mean)
ggplot(res, aes(x=Mean)) +
  geom_histogram(binwidth=.5, colour="black", fill="white") +
  geom_vline(aes(xintercept=mean(Mean, na.rm=T)),   # Ignore NA values for mean
             color="red", linetype="dashed", size=1)
