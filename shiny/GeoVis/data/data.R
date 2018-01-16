library(dplyr)

X <- read.csv('/Users/krishnakalyan3/Educational/PumpIt/data/original/train_set_values.csv')
y <- read.csv('/Users/krishnakalyan3/Educational/PumpIt/data/original/train_set_labels.csv')
X$id <- as.integer(X$id)
y$id <- as.integer(y$id)

join_data <- left_join(X, y, by=c('id'='id'))

app_dat <- join_data %>% select('id','longitude', 'latitude', 'date_recorded', 'status_group')

saveRDS(app_dat, file = "app_data.rds")
