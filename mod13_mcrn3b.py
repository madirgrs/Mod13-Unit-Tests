import unittest
from stock_data_visualizer import validate_symbol, validate_chart_type, validate_time_series, validate_date

class TestValidInputs(unittest.TestCase):

    def test_valid_symbol(self):
        self.assertTrue(validate_symbol('AAPL'))
        self.assertTrue(validate_symbol('GOOG'))

        self.assertFalse(validate_symbol('apple'))
        self.assertFalse(validate_symbol('aapl'))
        self.assertFalse(validate_symbol('1234567'))

    def test_valid_time_series(self):
        for i in ['1', '2', '3', '4']:
            self.assertTrue(validate_chart_type('i'))

        self.assertFalse(validate_chart_type('a'))
        self.assertFalse(validate_chart_type('0'))
        self.assertFalse(validate_chart_type('5'))

    def test_valid_chart_type(self):
        for i in ['1', '2']:
            self.assertTrue(validate_time_series('i'))
        
        self.assertFalse(validate_chart_type('a'))
        self.assertFalse(validate_chart_type('0'))
        self.assertFalse(validate_chart_type('3'))

    def test_valid_start_date(self):
        self.assertTrue(validate_date('2022-01-01', '2022-01-31'))

        self.assertFalse(validate_date('2022/01/01'))
        self.assertFalse(validate_date('01-01-2022'))
        self.assertFalse(validate_date('01-01-22'))

    def test_valid_end_date(self):
        self.assertTrue(validate_date('2022-01-01', '2022-01-31'))

        self.assertFalse(validate_date('2022/01/01'))
        self.assertFalse(validate_date('01-01-2022'))
        self.assertFalse(validate_date('01-01-22'))

if __name__ == '__main__':
    unittest.main()