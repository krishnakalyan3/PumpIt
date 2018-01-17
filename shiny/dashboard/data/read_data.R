library(dplyr)

X <- read.csv('/Users/krishnakalyan3/Educational/PumpIt/data/original/train_set_values.csv')
y <- read.csv('/Users/krishnakalyan3/Educational/PumpIt/data/original/train_set_labels.csv')
X$id <- as.integer(X$id)
y$id <- as.integer(y$id)

join_data <- left_join(X, y, by=c('id'='id'))
#str(join_data)

# select 3 numerical, 3 cateorigical values
cols_cat <- c('basin', 'waterpoint_type', 'quality_group', 'date_recorded')
cols_num <- c('construction_year', 'population', 'gps_height')
target <- c('status_group')

all_cols <- c(cols_cat, cols_num, target)
app_data <- select(join_data, all_cols)

saveRDS(app_data, file = "data/app_dashboard_data.rds")
