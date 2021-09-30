from django.test import TestCase
from django.urls import reverse, resolve
from ..views import projects, project
from ..models import Project
import uuid


class TestProjectList(TestCase):
    def test_projects_status_code(self):
        url = reverse('projects')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_projects_views_func(self):
        view = resolve('/project/')
        self.assertEqual(view.func, projects)


class TestSingleProduct(TestCase):
    def setUp(self):
        project = Project.objects.create(title='Title Test', 
            description='Description Test', 
            demo_link='http://example.com/dem',
            source_link='http://example.com/source', 
            vote_total=100, 
            vote_ratio=50
        )
        url = reverse('project', kwargs={'pk': Project.objects.first().id})
        self.response = self.client.get(url)

    def test_single_product_view_status_code(self):
        self.assertEqual(self.response.status_code, 200)
