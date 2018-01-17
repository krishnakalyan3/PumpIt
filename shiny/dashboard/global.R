library(shiny)
library(rCharts)

data_pump <- readRDS(file="data/app_dashboard_data.rds")
data_pump$population <- log(data_pump$population)
data_pump$construction_year <- log(data_pump$construction_year)
data_pump$gps_height <- log(data_pump$gps_height)
