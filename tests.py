import unittest
import data
import xls_parse

class TestSum(unittest.TestCase):

    def test_import_population1(self):
        xls_parsing_object = xls_parse.XLSParsing('Aruba')
        aruba_population = xls_parsing_object.import_country_population()
        self.assertEqual(aruba_population['1962:'], 56225, 'Should be 56225')

    def test_import_population2(self):
        xls_parsing_object = xls_parse.XLSParsing('France')
        france_population = xls_parsing_object.import_country_population()
        self.assertEqual(france_population['1969:'], 51638260, 'Should be 51638260')

    def test_import_co2_emissions1(self):
        xls_parsing_object = xls_parse.XLSParsing('Poland')
        poland_emissions = xls_parsing_object.import_country_co2_emissions()
        self.assertEqual(poland_emissions['1960:'], 199767, 'Should be 199767')

    def test_import_co2_emissions2(self):
        xls_parsing_object = xls_parse.XLSParsing('Sweden')
        sweden_emissions = xls_parsing_object.import_country_co2_emissions()
        self.assertEqual(sweden_emissions['2008:'], 49123, 'Should be 49123')


if __name__ == '__main__':
    unittest.main()
