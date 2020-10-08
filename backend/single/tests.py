from wagtail.tests.utils import WagtailPageTests
from wagtail.tests.utils.form_data import nested_form_data, \
    streamfield, rich_text
from wagtail.core.models import Page

from .models import SinglePage
from home.models import HomePage


# Create your tests here.
class SinglePageTests(WagtailPageTests):

    def test_can_create_a_page(self):
        """
        Test to see if I can create a page
        """
        root_page = HomePage.objects.first()

        self.assertCanCreate(root_page, SinglePage, nested_form_data({
            'title': 'About Test',
            'body': streamfield([
                ('title', 'About Test Page'),
                ('paragraph', rich_text('<p>This is my about test page.</p>')),
            ])
        }))

    def test_single_page_parent_pages(self):
        """
        Test to determine what parents
        a single page can have.
        """
        self.assertAllowedParentPageTypes(
            SinglePage,
            {Page, HomePage, SinglePage})
