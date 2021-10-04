from django.test import TestCase
from django.urls import reverse, resolve


class LoginViewTests(TestCase):
    def setUp(self):
        url = reverse("login")
        self.response = self.client.get(url)

    def test_login_view_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')


class RegisterViesTests(TestCase):
    def setUp(self):
        pass
