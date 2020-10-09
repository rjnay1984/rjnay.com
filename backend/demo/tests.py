from wagtail.tests.utils import WagtailPageTests
from wagtail.tests.utils.form_data import nested_form_data, rich_text
from wagtail.core.models import Page

from home.models import HomePage
from demo.models import DemoIndexPage

# Create your tests here.
class DemoTests(WagtailPageTests):

    def test_can_create_a_demo_index_page(self):
        """
        Test to see if I can create a page
        """
        root_page = HomePage.objects.first()

        self.assertCanCreate(root_page, DemoIndexPage, nested_form_data({
            'title': 'Demo Index Test',
            'intro': rich_text('Demo index test page.')
        }))

    def test_demo_index_page_parent_pages(self):
        """
        Test to determine what parents
        a demo index page can have.
        """
        self.assertAllowedParentPageTypes(
            DemoIndexPage,
            {Page, HomePage})
