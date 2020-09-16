from django.test import TestCase

from .models import HomePage


class HomePageTests(TestCase):

    def test_homepage_was_saved_with_body(self):
        """
        Homepage model can be saved with a body field.
        """
        body = 'Hello World!'
        home_page = HomePage(body=body)
        self.assertEqual(home_page.body, body)
