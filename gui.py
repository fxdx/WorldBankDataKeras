from guietta import Gui, Quit, _
import data
import xls_parse
import graph_plotting

gui = Gui( [ 'Enter country name' , '__country__' , ['Go'] ],
           [ 'Result ---> '       , 'result'      ,  Quit ] 
)

def population_plotting(country_name):
    country_info = data.CountryInformations(country_name)
    
    graph = graph_plotting.GraphPlotting(country_info)
    graph.plot_graph_population()

def submit_country_name(gui, *args):
    gui.result = gui.country

with gui.Go:
    population_plotting(gui.country)

gui.run()