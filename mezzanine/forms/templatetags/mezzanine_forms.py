from django import template
from mezzanine.forms.fields import RangeField, TitleField

register = template.Library()


@register.filter
def is_title_field(value):
    return isinstance(value, TitleField)


@register.filter
def is_range_field(value):
    return isinstance(value, RangeField)
