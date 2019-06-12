import pandas

class CountryInformations:

    def __init__(self, name):
        self.name = name

        xls_parsing = XLSParsing(self.name)

        self.population = xls_parsing.import_country_population()
        self.co2_emissions = xls_parsing.import_country_co2_emissions()
        self.renewable_electricity_status = xls_parsing.import_country_renewable_electricity_status()

    def __str__(self):

        return 'Country: {}, Population: {}, CO2 Emissions: {}, Renewable Electricity Status: {}'.format(self.name, \
                                                                                                         self.population, \
                                                                                                         self.co2_emissions, \
                                                                                                         self.renewable_electricity_status)


class XLSParsing:
    def __init__(self, name):

        self.name = name
        self.data = pandas.read_excel(r'API_19_DS2_en_excel_v2_10577512.xls')

    # Population, total
    def import_country_population(self):
        population = self.data.loc[
                    (self.data['Country Name:']==self.name)
                    & (self.data['Indicator Code:']=='SP.POP.TOTL')]

        return population

    # CO2 emissions (kt)
    def import_country_co2_emissions(self):
        co2_emissions = self.data.loc[(self.data['Country Name:']==self.name)
                                    & (self.data['Indicator Code:']=='EN.ATM.CO2E.KT')]

        return co2_emissions

    # Renewable electricity output (% of total electricity output)
    def import_country_renewable_electricity_status(self):
        renewable_electricity_status = self.data.loc[(self.data['Country Name:']==self.name)
                                                    & (self.data['Indicator Code:']=='EG.ELC.RNEW.ZS')]

        return renewable_electricity_status


if __name__ == "__main__":
    country = CountryInformations('Poland')
    print(country)
