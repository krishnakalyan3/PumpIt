


custom_js <- tags$head(includeCSS("style.css"),includeScript("gomap.js"))

title_panel <- h2('Data Explorer')    
status_groups <- c('all','functional','non functional','functional needs repair')
status_panel <- selectInput("target", "Status Group", status_groups)

sample_panel <- numericInput("samples", "Total Samples", 6000, min=10, max = 59400)

date_panel <- dateRangeInput("dater", "Date range:", 
                             start = "2002-10-01", end="2013-12-01")

panel_settings <- c(id = "controls", class = "panel panel-default", fixed = TRUE,
draggable = TRUE, top = 190, left = "auto", right = 20, bottom = "auto",
width = 330, height = "auto")

abs_panel <- absolutePanel(id = "controls", class = "panel panel-default", fixed = TRUE,
                           draggable = TRUE, top = 190, left = "auto", right = 20, 
                           bottom = "auto", width = 330, height = "auto", 
                           title_panel, status_panel, sample_panel, date_panel)


navbarPage(
  title = 'Geo Viz',
  tabPanel('GeoVis', custom_js, leafletOutput('map', height=1000), abs_panel),
  tabPanel('Data',   DT::dataTableOutput('dt1'))
)
