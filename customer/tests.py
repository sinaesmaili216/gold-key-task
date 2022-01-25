from django.contrib.auth import login
from django.contrib.auth.models import User
from django.test import TestCase


class LoginAndLogoutTest(TestCase):
    def setUp(self):
        self.credential = {
            'username': 'sina',
            'password': '123456'
        }
        user = User.objects.create_user(**self.credential)

    def test_login(self):
        response = self.client.post('http://127.0.0.1:8000/customer/login/', self.credential, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)

    def test_logout(self):
        self.client.post('http://127.0.0.1:8000/customer/login/', self.credential, follow=True)
        response = self.client.get('http://127.0.0.1:8000/customer/logout/')
        self.assertEqual(response.status_code, 302)


class RegisterTest(TestCase):
    def setUp(self):
        self.credential = {
         'username': 'sina',
         'password': '123456',
         'first_name': 'sina',
         'last_name': 'esmaili'
        }

    def test_register(self):
        response = self.client.post('http://127.0.0.1:8000/customer/register/', self.credential, follow=True)
        self.assertEqual(response.status_code, 200)

