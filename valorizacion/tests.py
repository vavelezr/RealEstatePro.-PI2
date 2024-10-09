from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Property
import unittest
import pandas as pd
from .arima_test import get_csv_data, get_model_data, arimax_prediction



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

class PropertyValuationTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser@example.com', password='12345')
        self.client.login(username='testuser@example.com', password='12345')
        self.form_data = {
            'neighbourhood': 'Calasanz',
            'direccion': '123 Calle Falsa',
            'type': 'apartamento',
            'num_rooms': 2,
            'num_banos': 1,
            'size': 80.0,
            'price_administration': 200.0,
            'age': 10,
            'garajes': 1,
            'stratum': 4,
        }

    def test_save_property_simple(self):
        property = Property.objects.create(
            user=self.user,
            neighbourhood='Calasanz',
            direccion='123 Calle Falsa',
            type='apartamento',
            num_rooms=2,
            num_banos=1,
            size=80.0,
            price_administration=200.0,
            age=10,
            garajes=1,
            stratum=4,
            estimated_price=500000.0,
        )
        self.assertIsNotNone(property)
        self.assertEqual(property.neighbourhood, 'Calasanz')
        self.assertEqual(property.type, 'apartamento')

    def test_save_property_with_missing_data(self):
        incomplete_data = self.form_data.copy()
        incomplete_data['num_rooms'] = ''  # Campo vacío
        
        response = self.client.post(reverse('calculate'), data=incomplete_data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Property.objects.filter(user=self.user).count(), 0)
        self.assertIn('num_rooms', response.context['form'].errors)

    def test_modify_saved_property(self):
        property = Property.objects.create(
            user=self.user,
            neighbourhood='Calasanz',
            direccion='123 Calle Falsa',
            type='apartamento',
            num_rooms=2,
            num_banos=1,
            size=80.0,
            price_administration=200.0,
            age=10,
            garajes=1,
            stratum=4,
            estimated_price=500000.0,
        )

        modified_data = self.form_data.copy()
        modified_data['num_rooms'] = 3
        modified_data['num_banos'] = 2
        modified_data['size'] = 90.0
        modified_data['age'] = 8

        response = self.client.post(reverse('edit_property', args=[property.id]), data=modified_data)

        self.assertEqual(response.status_code, 302)
        property.refresh_from_db()
        self.assertEqual(property.num_rooms, 3)
        self.assertEqual(property.num_banos, 2)
        self.assertEqual(property.size, 90.0)
        self.assertEqual(property.age, 8)

    def test_view_saved_property(self):
        property = Property.objects.create(
            user=self.user,
            neighbourhood='Calasanz',
            direccion='123 Calle Falsa',
            type='apartamento',
            num_rooms=2,
            num_banos=1,
            size=80.0,
            price_administration=200.0,
            age=10,
            garajes=1,
            stratum=4,
            estimated_price=500000.0,
        )

        response = self.client.get(reverse('profile'))

        self.assertContains(response, 'Calasanz')  # Verificar que el barrio aparece
        self.assertContains(response, 'apartamento')  # Verificar que el tipo de propiedad aparece
        self.assertContains(response, 2)  # Verificar el número de habitaciones
        self.assertContains(response, 1)  # Verificar el número de baños
        self.assertContains(response, '80,00 m²')  # Verificar el tamaño
        self.assertContains(response, '500000,00')  # Verificar el precio estimado

