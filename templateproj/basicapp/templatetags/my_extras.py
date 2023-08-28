from django import template

register = template.Library()

@register.filter(name='butt')
def butt(value,arg):
    """This cuts out all values of ARG from the string"""
    return value.replace(arg,'=|)')
