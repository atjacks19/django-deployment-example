from django import template

register = template.Library()

@register.filter('cutting', cutting)
def cutting(value,arg):
    """
    This cuts out all values of "arg" from the string!
    """

    return value.replace(arg,'')

# register.filter('cutting', cutting)
