from django import template
from django.template.defaultfilters import stringfilter
register = template.Library()

@register.filter(name = "errors_to_string")
def convert(data):
    if data == 1 :
        return 'Success'
    elif data == 2 :
        return 'Failure'
    else:
        return 'NonEnd'

@register.simple_tag
@stringfilter
def extract(data2,data):
    return data[:4]+data2


@register.inclusion_tag('about.html',takes_context = True )
def custominclusion (context):
    return { 'cook' : context['var1'] }