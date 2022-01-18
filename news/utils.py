

from .models import Category

pages = [
    {
        'title': 'About',
        'href': 'about'
    },
    {
        'title': 'Add Post',
        'href': 'addpost'
    },
    {
        'title': 'Contacts',
        'href': 'contacts'
    }
]

class DataMixin():
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()
        context['cats'] = cats
        context['menu'] = pages
        return context
