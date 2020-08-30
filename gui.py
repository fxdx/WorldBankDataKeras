from guietta import Gui, Quit, _, M, ___, III, R1
import matplotlib
import data
import xls_parse
import graph_plotting

gui = Gui( [ 'Enter country name'    ,                  '__country__'                     ,         ['Go']                     ],
           [    'Population'         , 'Renewable Electricity Status'                     ,  'Co2 Emissions'                   ],
           [ R1('population_button') ,       R1('renewable_electricity_status_button')    ,   R1('co2_emissions_button')       ],
           [            _            ,         _                                          ,  Quit                              ] 
)

def country_info_graph(country_name):
    country_info = data.CountryInformations(country_name)
    graph = graph_plotting.GraphPlotting(country_info)
    return graph

with gui.Go:
    plt = country_info_graph(gui.country)
    if gui.population_button.isChecked():
        plt.plot_graph_population()
    
    elif gui.renewable_electricity_status_button.isChecked():
        plt.plot_graph_renewable_electricity_status()
    
    elif gui.co2_emissions_button.isChecked():
        plt.plot_graph_co2_emissions()

gui.run()