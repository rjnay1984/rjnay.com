from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.api import APIField


class SinglePage(Page):
    """
    This is the model for a basic single page
    template with a PageBuilder/StreamField.
    """
    body = StreamField(
        [
            ('heading', blocks.CharBlock(classname="full title")),
            ('paragraph', blocks.RichTextBlock()),
            ('image', ImageChooserBlock()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    api_fields = [
        APIField('body')
    ]

    subpage_types = ['single.SinglePage']
