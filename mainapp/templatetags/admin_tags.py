from django import template

register = template.Library()


@register.simple_tag
def url_replace(request, field, value):
    """
    Replace (or add) a single query param while preserving all others.
    Usage: href="?{% url_replace request 'page' 3 %}"
    """
    params = request.GET.copy()
    params[field] = str(value)
    return params.urlencode()
