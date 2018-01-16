library(leaflet)

df <- readRDS(file="data/app_data.rds")
head(df)

unique(df$status_group)

leaflet(df) %>% addTiles() %>%  setView( 34.9, -9.85,zoom = 4) %>% 
  addCircles(~longitude, ~latitude, popup=df$status_group, weight = 1,
             color=c('red', 'blue', 'green'), stroke = TRUE) %>%
  addLegend("bottomright", colors=c('red', 'blue', 'green'), 
            labels=unique(df$status_group), title="Status")
