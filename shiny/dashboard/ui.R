library(plotly)

num_page <- fluidPage(plotlyOutput("plot1"), plotlyOutput("plot2"))
cat_page <- fluidPage(plotlyOutput("plot4"), plotlyOutput("plot5"), plotlyOutput("plot6"))

navbarPage(
  title = 'Dashboard',
  tabPanel('Numerical Values', num_page),
  tabPanel('Categorical Values', cat_page),
  tabPanel('Data Table',   DT::dataTableOutput('dtall'))
)
