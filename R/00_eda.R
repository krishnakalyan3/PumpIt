setwd('/Users/krishnakalyan3/Educational/PumpIt/data')
set.seed(123)
library(readr)
library(dplyr)
library(lightgbm)

train <- read_csv('train_set_values.csv')
glimpse(train)

dim(train)
# [1] 59400    40

y_train <- read_csv('train_set_labels.csv')