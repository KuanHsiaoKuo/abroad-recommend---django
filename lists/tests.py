from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page
from django.template.loader import render_to_string
from django.http import HttpRequest
import pdb
class HomePageTest(TestCase):
    def test_root_urlresolve_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func,home_page)
    def test_home_page_return_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(),expected_html)
