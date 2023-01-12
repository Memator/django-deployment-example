from django import template

register = template.Library()

@register.filter(name='cortar')
def cortar(value,arg):
    return value.replace(arg,'')

# register.filter('cortar',cortar)