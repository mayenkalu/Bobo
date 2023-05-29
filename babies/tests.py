from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse
from datetime import date
from dateutil.relativedelta import relativedelta
from .models import Baby

# Testing Baby model
class BabyModelTestCase(TestCase):
    def setUp(self):
        # Setting up user and baby for testing
        self.user = get_user_model().objects.create_user(username='testuser', password='testpass')
        self.baby = Baby.objects.create(
            user=self.user,
            name='Test Baby',
            gender='Male',
            date_of_birth=date.today() - relativedelta(months=6),
            weight=4.5,
            height=60.0,
            parent_name='Test Parent',
            parent_relationship='Father'
        )

    def test_model_creation(self):
        # Testing if the baby object is an instance of Baby model and the string representation of baby is the baby's name
        self.assertTrue(isinstance(self.baby, Baby))
        self.assertEqual(self.baby.__str__(), self.baby.name)

# Testing views for Baby model
class BabyViewsTestCase(TestCase):
    def setUp(self):
        # Setting up client, user, baby, and urls for testing
        self.client = Client()
        self.user = get_user_model().objects.create_user(username='testuser', password='testpass')
        self.baby = Baby.objects.create(
            user=self.user,
            name='Test Baby',
            gender='Male',
            date_of_birth='2020-01-01',
            weight=4.5,
            height=60.0,
            parent_name='Test Parent',
            parent_relationship='Father'
        )
        self.babies_journey_url = reverse('babies:babies_journey')
        self.baby_detail_url = reverse('babies:baby_detail', args=[self.baby.id])
        self.baby_update_url = reverse('babies:baby_update', args=[self.baby.id])
        self.baby_delete_url = reverse('babies:baby_delete', args=[self.baby.id])

    def test_baby_detail_view(self):
        # Testing the baby detail view
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.baby_detail_url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Baby')
        self.assertTemplateUsed(response, 'babies/baby_detail.html')

    def test_baby_update_view(self):
        # Testing the baby update view
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.baby_update_url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Baby')
        self.assertTemplateUsed(response, 'babies/baby_form.html')

    def test_baby_delete_view(self):
        # Testing the baby delete view
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.baby_delete_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'babies/baby_confirm_delete.html')

    def test_baby_create_view(self):
        # Testing the baby create view with a GET request and with a POST request to create a new baby
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('babies:baby_create'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'babies/baby_form.html')

        # Test POST request with valid data.
        response = self.client.post(reverse('babies:baby_create'), {
            'name': 'New Baby',
            'gender': 'Male',
            'date_of_birth': '2022-01-01',
            'weight': 5.0,
            'height': 65.0,
            'parent_name': 'Test Parent 2',
            'parent_relationship': 'Father'
        })
        self.assertEqual(response.status_code, 302)  # Check for redirect.
