from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import PropertyForm
from .models import RentalProperty

class RentalPropertyTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser@example.com', password='12345')
        self.client.login(username='testuser@example.com', password='12345')
        self.form_data = {
            'neighbourhood': 'castilla',
            'type': 'apartamento',
            'num_rooms': 2,
            'num_banos': 1,
            'size': 80,
            'age': 10,
            'wifi': 'on',
            'air_conditioner': '',
            'balcony': 'on',
            'terrace': '',
            'garden': '',
            'pool': '',
            'heater': 'on',
            'washing_machine': 'on',
            'dryer': '',
            'chimney': '',
            'jacuzzi': '',
            'sauna': '',
            'board_games': '',
            'parking': 'on',
        }

    def test_save_property_simple(self):
        property = RentalProperty.objects.create(
            user=self.user,
            neighbourhood='castilla',
            type='apartamento',
            num_rooms=2,
            num_banos=1,
            size=80,
            age=10,
            wifi=True,
            air_conditioner=False,
            balcony=True,
            terrace=False,
            garden=False,
            pool=False,
            heater=True,
            washing_machine=True,
            dryer=False,
            chimney=False,
            jacuzzi=False,
            sauna=False,
            board_games=False,
            parking=True,
            price_per_night=1000,
        )
        self.assertIsNotNone(property)
        self.assertEqual(property.neighbourhood, 'castilla')
        self.assertEqual(property.type, 'apartamento')

    def test_save_property_with_missing_data(self):
        incomplete_data = self.form_data.copy()
        incomplete_data['num_rooms'] = ''
        response = self.client.post(reverse('rent'), data=incomplete_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(RentalProperty.objects.filter(user=self.user).count(), 0)
        self.assertIn('num_rooms', response.context['form'].errors)

    def test_modify_saved_property(self):
        property = RentalProperty.objects.create(
            user=self.user,
            neighbourhood='castilla',
            type='apartamento',
            num_rooms=2,
            num_banos=1,
            size=80,
            age=10,
            wifi=True,
            air_conditioner=False,
            balcony=True,
            terrace=False,
            garden=False,
            pool=False,
            heater=True,
            washing_machine=True,
            dryer=False,
            chimney=False,
            jacuzzi=False,
            sauna=False,
            board_games=False,
            parking=True,
            price_per_night=1000,
        )
        modified_data = self.form_data.copy()
        modified_data['num_rooms'] = 3
        modified_data['num_banos'] = 2
        modified_data['size'] = 90
        modified_data['age'] = 8
        response = self.client.post(reverse('edit_rental_property', args=[property.id]), data=modified_data)
        self.assertEqual(response.status_code, 302)
        property.refresh_from_db()
        self.assertEqual(property.num_rooms, 3)
        self.assertEqual(property.num_banos, 2)
        self.assertEqual(property.size, 90)
        self.assertEqual(property.age, 8)

    def test_view_saved_property(self):
        property = RentalProperty.objects.create(
            user=self.user,
            neighbourhood='castilla',
            type='apartamento',
            num_rooms=2,
            num_banos=1,
            size=80,
            age=10,
            wifi=True,
            air_conditioner=False,
            balcony=True,
            terrace=False,
            garden=False,
            pool=False,
            heater=True,
            washing_machine=True,
            dryer=False,
            chimney=False,
            jacuzzi=False,
            sauna=False,
            board_games=False,
            parking=True,
            price_per_night=1000,
        )
        response = self.client.get(reverse('profile'))
        self.assertContains(response, 'castilla')
        self.assertContains(response, 2)
        self.assertContains(response, 1)
        self.assertContains(response, 'Sí')
        self.assertContains(response, '$1000,00')
