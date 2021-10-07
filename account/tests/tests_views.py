from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse, resolve


from ..views import profiles, userProfile
from ..models import Profile



class ProfilesPageTests(TestCase):
    def setUp(self):
        url = reverse('profiles')
        self.response = self.client.get(url)

    def test_profiles_view_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_profiles_view_resolve_view_func(self):
        view = resolve('/')
        self.assertEqual(view.func, profiles)
    
    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

class UserProfileTests(TestCase):
    def setUp(self):
        # self.user = User(username='JHorlamide', password='password')
        self.profile = Profile.objects.create(
            name='Olamide', 
            username='JHorlamide', 
            location='Lagos, Nigeria', 
            email='jhorlamide@gmail.com', 
            short_intro='Software Developer',
        )
        url = reverse('user_profile', kwargs={'pk': self.profile.id})
        self.response = self.client.get(url)
    
    def test_user_profile_view_status_code(self):
        self.assertEqual(self.response.status_code, 200)

class UserAccountTest(TestCase):
    def setUp(self):
        url = reverse('user_account')
        self.response = self.client.get(url)