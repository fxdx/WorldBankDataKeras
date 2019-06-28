import pandas
import matplotlib.pyplot as plt
import xls_parse
import graph_plotting

class CountryInformations:

    def __init__(self, name):
        self.name = name

        xls_parsing = xls_parse.XLSParsing(self.name)

        self.population = xls_parsing.import_country_population()
        self.co2_emissions = xls_parsing.import_country_co2_emissions()
        self.renewable_electricity_status = xls_parsing.import_country_renewable_electricity_status()

    def __str__(self):
        print_string = 'Country: {} \n \
                        Population: {} \n \
                        CO2 Emissions: {}KT \n \
                        Renewable Electricity Status: {}%'.format(self.name, \
                                                                  self.population, \
                                                                  self.co2_emissions, \
                                                                  self.renewable_electricity_status)
        return print_string


# Testing Purposes
if __name__ == "__main__":
    country1 = CountryInformations('Poland')
    country2 = CountryInformations('Germany')
    country3 = CountryInformations('France')

    graph = graph_plotting.GraphPlotting(country1, country2, country3)
    graph.plot_graph_co2_emissions()
    
