from django.test import TestCase
from django.urls import reverse, resolve
from ..views import projects, project
from ..models import Project
import uuid


class TestProjectList(TestCase):
    def setUp(self):
        url = reverse('projects')
        self.response = self.client.get(url)
        self.project = Project.objects.create(title='Title Test',
                                              description='Description Test',
                                              demo_link='http://example.com/dem',
                                              source_link='http://example.com/source',
                                              vote_total=100,
                                              vote_ratio=50
                                              )

    def test_projects_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_projects_views_func(self):
        view = resolve('/projects/')
        self.assertEqual(view.func, projects)

    # def test_projects_views_contain_link_to_single_project_view(self):
    #     project_url = reverse('project', kwargs={'pk': self.project.id})
    #     project_view_url = self.client.get(project_url)
    #     self.assertContains(self.response,
    #                         "href='{0}'".format(project_view_url), html=True)

    def test_project_view_contains_csrf_token(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')


class TestSingleProduct(TestCase):
    def setUp(self):
        self.project = Project.objects.create(title='Title Test',
                                              description='Description Test',
                                              demo_link='http://example.com/dem',
                                              source_link='http://example.com/source',
                                              vote_total=100,
                                              vote_ratio=50
                                              )
        url = reverse('project', kwargs={'pk': self.project.id})
        self.response = self.client.get(url)

    def test_single_product_view_status_code(self):
        self.assertEqual(self.response.status_code, 200)
