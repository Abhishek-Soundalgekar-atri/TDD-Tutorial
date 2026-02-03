from django.test import TestCase
from django.urls import resolve
from lists.views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_passes_all_items_to_template(self):
        response = self.client.get('/')
        self.assertIn('items', response.context)

    def test_home_page_shows_empty_list_when_no_items_exist(self):
        response = self.client.get('/')
        self.assertEqual(list(response.context['items']), [])
