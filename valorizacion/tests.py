import unittest
import pandas as pd
from arima_test import get_csv_data, get_model_data, arimax_prediction


class TestARIMAXIntegration(unittest.TestCase):

    def setUp(self):
        # Create mock data similar to what get_csv_data would return
        self.mock_data = pd.DataFrame({
            'id': [1, 2, 3],
            'neighbourhood': ['Downtown', 'Downtown', 'Suburb'],
            'rooms': [2, 3, 4],
            'baths': [1, 2, 3],
            'area': [50, 70, 100],
            'age': [1, 3, 2],
            'garages': [1, 2, 1],
            'stratum': [3, 4, 5],
            'price_x': [200000000, 350000000, 500000000],
            'year': pd.to_datetime(['2020', '2021', '2022'], format="%Y"),
        }).set_index('year')

    def test_get_csv_data(self):
        # Assume get_csv_data returns self.mock_data for testing
        data = get_csv_data()
        self.assertFalse(data.empty, "Data should not be empty")

    def test_get_model_data(self):
        # Test get_model_data with mock data
        neighbourhood = 'Downtown'
        filtered_data = get_model_data(self.mock_data, neighbourhood)
        self.assertFalse(filtered_data.empty, f"No data found for neighbourhood {neighbourhood}")
        self.assertTrue((filtered_data['neighbourhood'] == neighbourhood).all(), "Filtered data contains incorrect neighbourhood")

    def test_arimax_prediction(self):
        # Mock user data for prediction
        user_data_dict = {
            'neighbourhood': 'Downtown',
            'rooms': 2,
            'baths': 1,
            'area': 60,
            'age': 8,
            'garages': 1,
            'stratum': 3
        }
        predictions = arimax_prediction(user_data_dict, self.mock_data)
        self.assertIsNotNone(predictions, "Predictions should not be None")
        self.assertEqual(len(predictions), 6, "There should be 6 predictions")

if __name__ == '__main__':
    unittest.main()
