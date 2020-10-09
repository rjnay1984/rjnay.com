from wagtail.tests.utils import WagtailPageTests
from wagtail.core.models import Page
from wagtail.tests.utils.form_data import \
    nested_form_data, \
    rich_text

from .models import HomePage
from single.models import SinglePage
from demo.models import DemoIndexPage


class HomePageTests(WagtailPageTests):

    def test_can_create_homepage(self):
        """
        Homepage model can be saved with a body field.
        """
        root_page = Page.objects.first()

        self.assertCanCreate(root_page, HomePage, nested_form_data({
            'title': 'Test Home Page',
            'body': rich_text('This is my test homepage!')
        }))

    def test_home_page_subpages(self):
        """
        Test the subpages that can be created.
        """
        self.assertAllowedSubpageTypes(HomePage, {SinglePage, DemoIndexPage})
