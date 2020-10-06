from wagtail.tests.utils import WagtailPageTests
from wagtail.tests.utils.form_data import nested_form_data, \
    streamfield, rich_text
from .models import SinglePage
from home.models import HomePage


# Create your tests here.
class SinglePageTests(WagtailPageTests):

    def test_can_create_a_page(self):
        """
        Test to see if I can create a page
        """
        root_page = HomePage.objects.get(pk=3)

        self.assertCanCreate(root_page, SinglePage, nested_form_data({
            'title': 'About Test',
            'body': streamfield([
                ('title', 'About Test Page'),
                ('paragraph', rich_text('<p>This is my about test page.</p>')),
            ])
        }))
