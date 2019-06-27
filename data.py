import pandas
import matplotlib.pyplot as plt
import xls_parse

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

    def plot_graph(self, x_data, y_data, y_axis_info, title):
        figure_plot = plt.figure()

        main_graph = figure_plot.add_subplot(111)

        main_graph.plot(x_data, 
                        y_data, 
                        color='lightcoral', 
                        linewidth=3,
                        linestyle='--')

        main_graph.set_xlim(x_data[0], x_data[-1])

        plt.title(title)
        plt.xlabel('Year')
        plt.ylabel(y_axis_info)

        plt.show(main_graph)


# Testing Purposes
if __name__ == "__main__":
    country = CountryInformations('Poland')
    country.plot_graph(list(country.co2_emissions.keys()), 
                       list(country.co2_emissions.values()), 'CO2 Emissions (KT)', 
                       '{} CO2 Emissions'.format(country.name))
