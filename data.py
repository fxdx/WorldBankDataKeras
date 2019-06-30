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
        self.co2_emissions = xls_parsing.import_country_co2_emissions()
        self.renewable_electricity_status = xls_parsing.import_country_renewable_electricity_status()

        # I want to have linear regression values in format [year] : value
        self.population_linear_regression = self.population.copy()
        self.co2_emissions_linear_regression = self.co2_emissions.copy()
        self.renewable_electricity_status_linear_regression = self.renewable_electricity_status.copy()

        linear = linear_regr.LinearRegression(list(self.population_linear_regression.values()))
        # Replacing values in dict by values from linear regression
        self.population_linear_regression = dict.fromkeys(self.population_linear_regression,
                                                          linear.return_values_of_linear_regression())

        linear = linear_regr.LinearRegression(list(self.co2_emissions_linear_regression.values()))
        # Replacing values in dict by values from linear regression
        self.co2_emissions_linear_regression = dict.fromkeys(self.co2_emissions_linear_regression,
                                                             linear.return_values_of_linear_regression())

        linear = linear_regr.LinearRegression(list(self.renewable_electricity_status_linear_regression.values()))
        # Replacing values in dict by values from linear regression
        self.renewable_electricity_status_linear_regression = dict.fromkeys(self.renewable_electricity_status_linear_regression, 
                                                                            linear.return_values_of_linear_regression())

    def __str__(self):
        print_string = 'Country: {} \n \
                        Population: {}M \n \
                        CO2 Emissions: {}KT \n \
                        Renewable Electricity Status: {}%'.format(self.name, \
                                                                  self.population, \
                                                                  self.co2_emissions, \
                                                                  self.renewable_electricity_status)
        return print_string

    
