import unittest
from unittest.mock import patch

from Project3 import get_stock_symbol, get_chart_type, get_time_series_function, get_date_range

class StockVisualizerSymbolTests(unittest.TestCase):

    # we focus on unit testing for existing functionality that was submitted
    # for project 3. Given the conditions, modified the Project 3 get_stock_symbol()
    # to take 1 to 7 alpha charcters only
    @patch('builtins.input', side_effect=['MSFT', 'tsla', 'AAPL'])
    def test_valid_stock_symbol(self, mock_input):
        self.assertEqual(get_stock_symbol(), 'MSFT')
        self.assertEqual(get_stock_symbol(), 'TSLA')
        self.assertEqual(get_stock_symbol(), 'AAPL')

    @patch('builtins.input', side_effect=['123@', 'ABCDEFGH', 'MSFT'])
    def test_invalid_stock_symbol(self, mock_input):
        self.assertEqual(get_stock_symbol(), 'MSFT')
        # Because after two invalid tries (123 and ts23), third input 'MSFT' must be accepted

    @patch('builtins.input', side_effect=['123$', 'TSLA'])
    def test_invalid_then_valid_stock_symbol(self, mock_input):
        self.assertEqual(get_stock_symbol(), 'TSLA')

class StockVisualizerChartTypeTests(unittest.TestCase):
    @patch('builtins.input', return_value='1')
    def test_select_chart_type_line(self, mock_input):
        self.assertEqual(get_chart_type(), 'Line Chart')

    @patch('builtins.input', return_value='2')
    def test_select_chart_type_bar(self, mock_input):
        self.assertEqual(get_chart_type(), 'Bar Chart')

    # Only asked for chart type 1 or 2
    # @patch('builtins.input', return_value='3')
    # def test_select_chart_type_candlestick(self, mock_input):
    #     self.assertEqual(get_chart_type(), 'Candlestick Chart')

    @patch('builtins.input', side_effect=['5', '2'])
    def test_invalid_then_valid_chart_type_choice(self, mock_input):
        self.assertEqual(get_chart_type(), 'Bar Chart')


class StockVisualizerTimeSeriesTests(unittest.TestCase):
    @patch('builtins.input', return_value='2')
    def test_select_intraday(self, mock_input):
        func, interval = get_time_series_function()
        self.assertEqual(func, "TIME_SERIES_INTRADAY")
        self.assertEqual(interval, "5min")


    @patch('builtins.input', return_value='2')
    def test_select_daily(self, mock_input):
        func, interval = get_time_series_function()
        self.assertEqual(func, "TIME_SERIES_DAILY")
        self.assertIsNone(interval)


    @patch('builtins.input', return_value='3')
    def test_select_weekly(self, mock_input):
        func, interval = get_time_series_function()
        self.assertEqual(func, "TIME_SERIES_WEEKLY")
        self.assertIsNone(interval)


    @patch('builtins.input', return_value='4')
    def test_select_monthly(self, mock_input):
        func, interval = get_time_series_function()
        self.assertEqual(func, "TIME_SERIES_MONTHLY")
        self.assertIsNone(interval)


    @patch('builtins.input', side_effect=['5', '2'])
    def test_invalid_then_valid_time_series(self, mock_input):
        func, interval = get_time_series_function()
        self.assertEqual(func, "TIME_SERIES_DAILY")
        self.assertIsNone(interval)

class TestStartEndDateRange(unittest.TestCase):

    # we will test start and end date mocking how Project 3 takes 2 inputs
    @patch('builtins.input', side_effect=['2024-04-01', '2024-04-25'])
    def test_valid_date_range(self, mock_input):
        start, end = get_date_range()
        self.assertEqual(start, '2024-04-01')
        self.assertEqual(end, '2024-04-25')

    @patch('builtins.input', side_effect=['2024-04-25', '2024-04-01', '2024-04-01', '2024-04-25'])
    def test_end_date_before_start_date_then_valid(self, mock_input):
        start, end = get_date_range()
        self.assertEqual(start, '2024-04-01')
        self.assertEqual(end, '2024-04-25')

    @patch('builtins.input', side_effect=['04-01-2024', '2024-04-25', '2024-04-01', '2024-04-25'])
    def test_invalid_start_date_format_then_valid(self, mock_input):
        start, end = get_date_range()
        self.assertEqual(start, '2024-04-01')
        self.assertEqual(end, '2024-04-25')

    @patch('builtins.input', side_effect=['2024-04-01', '04-25-2024', '2024-04-01', '2024-04-25'])
    def test_invalid_end_date_format_then_valid(self, mock_input):
        start, end = get_date_range()
        self.assertEqual(start, '2024-04-01')
        self.assertEqual(end, '2024-04-25')

if __name__ == "__main__":
    unittest.main()



