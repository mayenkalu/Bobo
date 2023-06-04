# tests.py
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Category, Item
from .forms import ItemForm

from PIL import Image
from io import BytesIO
from django.core.files.images import ImageFile

# Create your tests here.

User = get_user_model()


class ItemModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.test_category = Category.objects.create(name='Test Category')
        cls.test_user = get_user_model().objects.create_user(username='testuser', password='12345')
        cls.test_item = Item.objects.create(
            name='Test Item', 
            description='Test Description', 
            contact='Test Contact', 
            price=100.00, 
            image=None, 
            category=cls.test_category, 
            user=cls.test_user
            
        )

    def test_item_name(self):
        self.assertEqual(self.test_item.name, 'Test Item')

    def test_item_description(self):
        self.assertEqual(self.test_item.description, 'Test Description')

    def test_item_contact(self):
        self.assertEqual(self.test_item.contact, 'Test Contact')

    def test_item_price(self):
        self.assertEqual(self.test_item.price, 100.00)

    def test_item_category(self):
        self.assertEqual(self.test_item.category, self.test_category)

    def test_item_user(self):
        self.assertEqual(self.test_item.user, self.test_user)

class ItemFormTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Category 1')

        self.data = {
            'name': 'Test item',
            'description': 'Some description',
            'contact': 'test@example.com',
            'price': '100.00',
            'category': self.category.id,
        }

    def test_form_item_name_label(self):
        form = ItemForm(data=self.data)
        self.assertEqual(form.fields['name'].label, 'Name')

