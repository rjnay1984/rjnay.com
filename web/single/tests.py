from wagtail.tests.utils import WagtailPageTests
from .models import SinglePage
from home.models import HomePage

# Create your tests here.
class SinglePageTests(WagtailPageTests):

    def test_can_create_a_page(self):
        """
        Test to see if I can create a page
        """
        self.assertCanCreateAt(HomePage, SinglePage)