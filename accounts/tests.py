from django.test import TestCase, Client
from .models import User
from django.urls import reverse

# AuthTestCase is a class where we define a suite of tests related to user authentication
class AuthTestCase(TestCase):
    # setUp is a special method that sets up the state for each test in this suite.
    # Here, it creates a test client and a test user.
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@test.com',
            password='testpassword'
        )

    # This test checks if the signup view is working by making a GET request to the 'signup' URL.
    # It checks if the response has a status code of 200 and if it used the correct template.
    def test_signup_view(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/signup.html')

    # This test checks the signup view's POST handling by sending a POST request with user data.
    # It checks if the response has a status code of 302 (redirect) and if it redirects to the correct URL.
    def test_signup_view_post(self):
        response = self.client.post(reverse('signup'), {
            'username': 'testuser2',
            'email': 'testuser2@test.com',
            'password1': 'testpassword2',
            'password2': 'testpassword2',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

    # The next two tests are equivalent to the signup tests, but for the login view.
    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')

    def test_login_view_post(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpassword',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

    # This test checks if the home view is accessible for logged-in users.
    def test_home_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/home.html')

    # This test checks if the logout view logs out the user and redirects them to the login page.
    def test_logout_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))

    # This test checks if the delete_account view redirects the user to the confirmation page.
    def test_delete_account_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('delete_account'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('delete_account_confirm'))

    # The next two tests are equivalent to the login tests, but for the delete_account_confirm view.
    def test_delete_account_confirm_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('delete_account_confirm'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/delete_account_confirm.html')

    def test_delete_account_confirm_view_post(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('delete_account_confirm'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
