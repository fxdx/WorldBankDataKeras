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
        plt.title('co2 emissions over years')
        plt.xlabel('Year')
        plt.ylabel('co2 emissions')

        plt.show()