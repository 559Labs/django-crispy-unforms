from __future__ import unicode_literals

from django.template import Template
from django.template.loader import render_to_string
from django.utils.html import conditional_escape

from crispy_forms.compatibility import string_types, text_type
from crispy_forms.utils import render_field, flatatt, TEMPLATE_PACK, get_template_pack


class Thumbnail(object):
    """
    Layout object. It takes a single field (which should be a URL).

    You can set `css_id` for a DOM id and `css_class` for a DOM class. Example::

        Thumbnail('form_field_url', css_id='myid', css_class='myclass')
    """

    def __init__(self, url, name, caption=False):
        self._url = url
        self._name = name
        self._caption = caption

    def render(self, form, form_style, context, template_pack=TEMPLATE_PACK, **kwargs):
        html = []
        html.append('<div class="thumbnail">')
        html.append('<img src="{{ object.' + self._url +
                    ' }}" alt="{{ object.' + self._name + ' }}" />')
        if self._caption:
            html.append(
                '<div class="caption"><h3>{{ object.' +
                self._name + ' }}</h3></div>'
            )
        html.append('</div>')
        html = "".join(html)
        return Template(text_type(html)).render(context)
