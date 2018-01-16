

function(input, output) {
  
  status_filter <- reactive({
    data <- data[1:input$samples,]
    if(input$target == 'all'){
      data <- data
      }
    else{
      data[data$status_group == input$target,]
    }
  })
  
  colorpal <- reactive({
    colorFactor(c('red', 'blue', 'green'), data$status_group)
  })

  output$dt1 <- DT::renderDataTable(
    DT::datatable(data, options = list(pageLength = 10))
  )
  
  output$map <- renderLeaflet({
    pal <- colorpal()
    
    leaflet(data) %>% addTiles() %>%  
      setView( 34.9, -9.85,zoom = 6) %>% 
      addCircles(~longitude, ~latitude,  
                 weight=1, color=pal(data$status_group))
  })
  
  observe({
    data <- status_filter()
    pal <- colorpal()
    leafletProxy("map", data =data)  %>% addTiles() %>%  
      clearShapes()  %>% 
      addCircles(~longitude, ~latitude,  
                 weight=1, color=pal(data$status_group))
  })
  
  

}

