import pandas

class XLSParsing:
    
    def __init__(self, name):

        self.name = name
        self.data = pandas.read_excel(r'API_19_DS2_en_excel_v2_10577512.xls')
        self.unnecessary_columns = ('Country Name:', 'Country Code:', 'Indicator Name:', 'Indicator Code:')

    def dropping_nan(self, dictionary_to_check):
        new_dict = dict()
        for key in dictionary_to_check.keys():
            try:
                new_dict[key] = int(dictionary_to_check[key])
            except:
                pass

        return new_dict

    # Population, total
    def import_country_population(self):
        population = self.data.loc[(self.data['Country Name:']==self.name)
                                & (self.data['Indicator Code:']=='SP.POP.TOTL')]

        for column in population:
            if column in self.unnecessary_columns:
                del population[column]

        population = population.to_dict()

        '''
        It is now in dict  {year : { index : value}} format so I need to get 
        dict {year : value} format
        '''
        for pop_key in population.keys():
            for value_key in population[pop_key].keys():
                population[pop_key] = population[pop_key][value_key]
        

        population = self.dropping_nan(population)
        return population

    # CO2 emissions (kt)
    def import_country_co2_emissions(self):
        co2_emissions = self.data.loc[(self.data['Country Name:']==self.name)
                                    & (self.data['Indicator Code:']=='EN.ATM.CO2E.KT')]

        for column in co2_emissions:
            if column in self.unnecessary_columns:
                del co2_emissions[column]

        co2_emissions = co2_emissions.to_dict()

        '''
        It is now in dict  {year : { index : value}} format so I need to get 
        dict {year : value} format
        '''
        for pop_key in co2_emissions.keys():
            for value_key in co2_emissions[pop_key].keys():
                co2_emissions[pop_key] = co2_emissions[pop_key][value_key]
        
        co2_emissions = self.dropping_nan(co2_emissions)
        return co2_emissions

    # Renewable electricity output (% of total electricity output)
    def import_country_renewable_electricity_status(self):
        renewable_electricity_status = self.data.loc[(self.data['Country Name:']==self.name)
                                                    & (self.data['Indicator Code:']=='EG.ELC.RNEW.ZS')]

        for column in renewable_electricity_status:
            if column in self.unnecessary_columns:
                del renewable_electricity_status[column]
        
        renewable_electricity_status = renewable_electricity_status.to_dict()

        '''
        It is now in dict  {year : { index : value}} format so I need to get 
        dict {year : value} format
        '''
        for pop_key in renewable_electricity_status.keys():
            for value_key in renewable_electricity_status[pop_key].keys():
                renewable_electricity_status[pop_key] = renewable_electricity_status[pop_key][value_key]
        

        renewable_electricity_status = self.dropping_nan(renewable_electricity_status)
        return renewable_electricity_status