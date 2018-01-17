


function(input, output) {
  
  
  output$dtall <- DT::renderDataTable(
    DT::datatable(data_pump, options = list(pageLength = 10))
  )
  
  output$plot1 <- plotly::renderPlotly({
    plot_ly(x=data_pump$construction_year, color=data_pump$status_group, type = 'histogram') 
  })
  
  output$plot2 <- plotly::renderPlotly({
    plot_ly(x=data_pump$gps_height, color=data_pump$status_group,  type = 'histogram')
  })
  
  output$plot4 <- plotly::renderPlotly({
    plot_ly(x =data_pump$basin,  color =data_pump$status_group, type = 'histogram')
  })
  
  output$plot5 <- plotly::renderPlotly({
    plot_ly(x =data_pump$waterpoint_type, color =data_pump$status_group, type = 'histogram')
  })
  
  output$plot6 <- plotly::renderPlotly({
    plot_ly(x=data_pump$quality_group, color=data_pump$status_group, type = 'histogram')
  })
  
}