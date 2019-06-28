import matplotlib.pyplot as plt
import numpy

class GraphPlotting:
    def __init__(self, *args):
        self.country_objects = []
        for country in args:
            self.country_objects.append(country)

    def plot_graph_co2_emissions(self):
        figure_plot = plt.figure(figsize=(16,9))

        for country in self.country_objects:

            main_graph = figure_plot.add_subplot(111)

            main_graph.scatter(list(country.co2_emissions.keys()),
                               list(country.co2_emissions.values()),
                               label=country.name,
                               c=numpy.random.rand(3,))
            
            main_graph.set_xlim(list(country.co2_emissions.keys())[0], 
                                list(country.co2_emissions.keys())[-1])

        plt.legend(loc='upper left')
        plt.tick_params(axis='x', rotation=70)
        plt.title('CO2 Emissions Over Years')
        plt.xlabel('Year')
        plt.ylabel('Co2 emissions')
        plt.show()

    def plot_graph_population(self):
        figure_plot = plt.figure(figsize=(16,9))

        for country in self.country_objects:

            main_graph = figure_plot.add_subplot(111)

            main_graph.scatter(list(country.population.keys()),
                               list(country.population.values()),
                               label=country.name,
                               c=numpy.random.rand(3,))
            
            main_graph.set_xlim(list(country.population.keys())[0], 
                                list(country.population.keys())[-1])

        plt.legend(loc='upper left')
        plt.tick_params(axis='x', rotation=70)
        plt.title('Population Over Years')
        plt.xlabel('Year')
        plt.ylabel('Population')
        plt.show()

    def plot_graph_renewable_electricity_status(self):
        figure_plot = plt.figure(figsize=(16,9))

        for country in self.country_objects:

            main_graph = figure_plot.add_subplot(111)

            main_graph.scatter(list(country.renewable_electricity_status.keys()),
                               list(country.renewable_electricity_status.values()),
                               label=country.name,
                               c=numpy.random.rand(3,))
            
            main_graph.set_xlim(list(country.renewable_electricity_status.keys())[0], 
                                list(country.renewable_electricity_status.keys())[-1])

        plt.legend(loc='upper left')
        plt.tick_params(axis='x', rotation=70)
        plt.title('Renewable Electricity % Over Years')
        plt.xlabel('Year')
        plt.ylabel('Renewable Electricity %')
        plt.show()

    

    