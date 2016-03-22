from django import template
import json

# # from django.template.defaultfilters import register
# # from setuptools.command import register
#
register = template.Library()


@register.filter
def tojson(value):
	return json.dumps(value)