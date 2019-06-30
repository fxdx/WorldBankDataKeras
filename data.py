import pandas
import matplotlib.pyplot as plt
import xls_parse
import graph_plotting
import linear_regr

class CountryInformations:

    def __init__(self, name):
        self.name = name

        xls_parsing = xls_parse.XLSParsing(self.name)
        
        self.population = xls_parsing.import_country_population()
        # Dividing by 10^6 to have smaller values (important during calculating linear regression)
        for key in self.population:
            self.population[key] = self.population[key] / 1000000

        self.co2_emissions = xls_parsing.import_country_co2_emissions()
        # Dividing by 10^3 to have smaller values (important during calculating linear regression)
        for key in self.co2_emissions:
            self.co2_emissions[key] = self.co2_emissions[key] / 1000

        self.renewable_electricity_status = xls_parsing.import_country_renewable_electricity_status()

        # I want to have linear regression values in format [year] : value
        self.population_linear_regression = self.population.copy()
        self.co2_emissions_linear_regression = self.co2_emissions.copy()
        self.renewable_electricity_status_linear_regression = self.renewable_electricity_status.copy()

        linear = linear_regr.LinearRegression(list(self.population_linear_regression.values()))
        # Replacing values in dict by values from linear regression
        values = linear.return_values_of_linear_regression()
        for i in range(0, len(values)):
            values[i] = int(values[i])
        
        # simple variable indexing values
        i=0
        for key in self.population_linear_regression.keys():
            self.population_linear_regression[key] = values[i]
            i = i+1

        linear = linear_regr.LinearRegression(list(self.co2_emissions_linear_regression.values()))
        # Replacing values in dict by values from linear regression
        values = linear.return_values_of_linear_regression()
        for i in range(0, len(values)):
            values[i] = int(values[i])
        
        # simple variable indexing values
        i=0
        for key in self.co2_emissions_linear_regression.keys():
            self.co2_emissions_linear_regression[key] = values[i]
            i = i+1

        linear = linear_regr.LinearRegression(list(self.renewable_electricity_status_linear_regression.values()))
        # Replacing values in dict by values from linear regression
        values = linear.return_values_of_linear_regression()
        for i in range(0, len(values)):
            values[i] = int(values[i])
        
        # simple variable indexing values
        i=0
        for key in self.renewable_electricity_status_linear_regression.keys():
            self.renewable_electricity_status_linear_regression[key] = values[i]
            i = i+1

    def __str__(self):
        print_string = 'Country: {} \n \
                        Population: {} milions \n \
                        CO2 Emissions: {}GT \n \
                        Renewable Electricity Status: {}%'.format(self.name, \
                                                                  self.population, \
                                                                  self.co2_emissions, \
                                                                  self.renewable_electricity_status)
        return print_string

    
