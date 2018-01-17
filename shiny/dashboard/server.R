


function(input, output) {
  
  
  output$dt1 <- DT::renderDataTable(
    DT::datatable(data_pump, options = list(pageLength = 10))
  )
  
  output$plot1 <- renderPlotly({
    plot_ly(data_pump, x = ~construction_year,  color = ~status_group, type = 'histogram') 
  })
  
  output$plot2 <- renderPlotly({
    plot_ly(data_pump, x = ~gps_height, color = ~status_group,  type = 'histogram')
  })
  
  output$plot3 <- renderPlotly({
    plot_ly(data_pump, x = ~population, color = ~status_group, type = 'histogram')
  })
  
  output$plot4 <- renderPlotly({
    plot_ly(data_pump, x = ~basin,  color = ~status_group, type = 'histogram')
  })
  
  output$plot5 <- renderPlotly({
    plot_ly(data_pump, x = ~waterpoint_type, color = ~status_group, type = 'histogram')
  })
  
  output$plot6 <- renderPlotly({
    plot_ly(data_pump, x = ~quality_group, color = ~status_group, type = 'histogram')
  })

  
}