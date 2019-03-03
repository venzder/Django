from django import template
from django.core.paginator import Paginator
from django.template.loader import render_to_string

register = template.Library()


@register.inclusion_tag('pagination/pagination.html', name='pagination', takes_context=True)
def render_pagination(context, value, num=10):
    request = context.get('request')
    page = request.GET.get('page')
    paginator = Paginator(value, num)
    return {
        'page_obj': paginator.get_page(page),
        'paginator': paginator
        }


@register.filter(name='paginate')
def paginate_value(value, page, num=10):

    paginator = Paginator(value, num)
    return paginator.get_page(page)

