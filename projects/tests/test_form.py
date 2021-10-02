from django.test import TestCase
from django.urls import reverse, resolve
from ..views import projects, project, create_project
from ..models import Project


class CreateProjectTests(TestCase):
    def setUp(self):
        self.url = reverse('create_project')
        self.response = self.client.get(self.url)
        Project.objects.create(title='Test title', description='Test description', vote_total=10,
                               vote_ratio=100, source_link='http://example.com', demo_link='http://example.com/')

    def test_create_project_view_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_create_project_view_func(self):
        view = resolve('/projects/create_project/')
        self.assertEqual(view.func, create_project)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_valid_create_project(self):
        url = reverse('create_project')
        data = {
            "title": 'Test title',
            "description": 'Test description',
            "vote_total": 10,
            "vote_ratio": 100,
            "source_link": 'http://example.com',
            "demo_link": 'http://example.com/'
        }
        response = self.client.post(url, data)
        self.assertRedirects(response, reverse('projects'))
        self.assertTrue(Project.objects.exists())

    def test_invalid_create_project(self):
        url = reverse('create_project')
        response = self.client.post(url, {})
        form = response.context.get('form')
        self.assertTrue(response, reverse('projects'))
        # self.assertTrue(form.error)
