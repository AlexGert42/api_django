from django import template
from django.contrib.auth.models import User
from news.models import *

register = template.Library()


# @register.simple_tag()
# def get_caterories():
#     return Category.objects.all()


@register.inclusion_tag('news/header/navbar.html')
def show_navbar():
    category = Category.objects.all()
    return {'category': category}


# @register.inclusion_tag('news/header/header.html')
# def show_header():
#     pages = [
#         {
#             'title': 'About',
#             'href': 'about'
#         },
#         {
#             'title': 'Add Post',
#             'href': 'addpost'
#         },
#         {
#             'title': 'Contacts',
#             'href': 'contacts'
#         }
#     ]
#     return {'menu': pages}
