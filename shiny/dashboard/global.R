library(shiny)
library(plotly)

data_pump <- readRDS(file="data/app_dashboard_data.rds")
data_pump$population <- log(data$population)
data_pump$construction_year <- log(data$construction_year)
data_pump$gps_height <- log(data$gps_height)

