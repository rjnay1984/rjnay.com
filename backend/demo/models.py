from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.search import index


class DemoIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    search_fields = Page.search_fields + [
        index.SearchField('intro')
    ]

    subpage_types = ['demo.DemoPage']


class DemoPage(Page):
    teaser = RichTextField(blank=True)
    link = models.URLField()
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('teaser', classname="full"),
        FieldPanel('link', classname="full"),
        FieldPanel('body', classname="full")
    ]

    search_fields = Page.search_fields + [
        index.SearchField('teaser'),
        index.SearchField('body')
    ]

    subpage_types = []
